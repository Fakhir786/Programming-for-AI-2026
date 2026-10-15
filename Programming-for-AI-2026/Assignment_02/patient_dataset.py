from pathlib import Path
import json
import pandas as pd
import numpy as np

# columns the dataset has to have, otherwise nothing else matters
REQUIRED_COLS = ["patient_id", "age", "heart_rate", "department"]

# these show up as literal strings in the CSV, treat them as empty
MISSING_VALS = ["", "missing", "N/A", "-"]


class PatientDataset:
    def __init__(self, path):
        self.path = Path(path)
        self.raw = pd.read_csv(
            self.path,
            na_values=MISSING_VALS,
            dtype={"patient_id": "string"},  # keep IDs as strings, don't let pandas guess
        )

    def validate_required(self, columns):
        missing = [c for c in columns if c not in self.raw.columns]
        if missing:
            # fail loudly instead of silently producing garbage downstream
            raise ValueError(f"Missing columns: {missing}")

    def audit(self):
        self.validate_required(REQUIRED_COLS)

        rows, cols = self.raw.shape

        # blanks per column
        missing_counts = {c: self.raw[c].isna().sum() for c in self.raw.columns}

        # identical rows (all columns match)
        exact_dups = self.raw.duplicated().sum()

        # two rows can differ in some column but still be the same patient,
        # so drop exact dupes first and then look for repeated IDs
        deduped = self.raw.drop_duplicates()
        repeated_ids = deduped.duplicated(subset=["patient_id"]).sum()

        # sanity ranges for the numeric fields
        limits = {"age": (0, 120), "heart_rate": (30, 220)}
        nonnumeric_counts = {}
        invalid_value_counts = {}

        for col, (low, high) in limits.items():
            if col not in self.raw.columns:
                # column missing entirely, nothing to check
                nonnumeric_counts[col] = 0
                invalid_value_counts[col] = 0
                continue

            as_num = pd.to_numeric(self.raw[col], errors="coerce")
            # anything that was there but became NaN = couldn't be parsed as a number
            nonnumeric_counts[col] = self.raw[col].notna().sum() - as_num.notna().sum()

            valid = as_num.dropna()
            invalid_value_counts[col] = ((valid < low) | (valid > high)).sum()

        if "department" in self.raw.columns:
            dept_labels = sorted(self.raw["department"].dropna().astype(str).unique())
        else:
            dept_labels = []

        # wrap everything in int() so json.dump doesn't choke on numpy int64
        return {
            "row_count": int(rows),
            "column_count": int(cols),
            "missing_counts": {k: int(v) for k, v in missing_counts.items()},
            "exact_duplicate_count": int(exact_dups),
            "repeated_id_count": int(repeated_ids),
            "invalid_value_counts": {k: int(v) for k, v in invalid_value_counts.items()},
            "nonnumeric_counts": {k: int(v) for k, v in nonnumeric_counts.items()},
            "department_labels": dept_labels,
        }

    def cleaned(self):
        self.validate_required(REQUIRED_COLS)

        df = self.raw.copy()
        df = df.drop_duplicates().reset_index(drop=True)

        # patient_id has to be a clean unique string
        df["patient_id"] = df["patient_id"].astype(str).str.strip()

        if df["patient_id"].isna().any() or (df["patient_id"] == "").any():
            raise ValueError("Found invalid or missing patient IDs.")
        if df["patient_id"].duplicated().any():
            # if two rows point to the same patient, we can't safely merge them
            raise ValueError("Duplicate patient IDs found after cleaning.")

        # department: trim whitespace, upper-case, then map the variants
        df["department"] = df["department"].astype(str).str.strip().str.upper()

        aliases = {
            "GEN MED": "GENERAL MEDICINE",
            "GENERAL MED": "GENERAL MEDICINE",
            "GENERAL-MED": "GENERAL MEDICINE",
            "CARDIO": "CARDIOLOGY",
        }
        df["department"] = df["department"].replace(aliases)

        # after uppercasing, some missing values end up as "NAN"/"NONE" strings,
        # so replace those before fillna picks up actual NaNs
        junk = ["NAN", "NAT", "NONE", "MISSING", "N/A", "-"]
        df["department"] = df["department"].replace(junk, "Unknown")
        df["department"] = df["department"].fillna("Unknown")

        # force numerics – anything unparseable becomes NaN
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
        df["heart_rate"] = pd.to_numeric(df["heart_rate"], errors="coerce")

        # out of range = treat as missing
        df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = np.nan
        df.loc[(df["heart_rate"] < 30) | (df["heart_rate"] > 220), "heart_rate"] = np.nan

        # flag which cells we're about to fill so it's traceable
        df["age_imputed"] = df["age"].isna()
        df["heart_rate_imputed"] = df["heart_rate"].isna()

        # fill with median of the valid values (more robust than mean here)
        for col, low, high in [("age", 0, 120), ("heart_rate", 30, 220)]:
            valid = df[(df[col] >= low) & (df[col] <= high)][col]
            df[col] = df[col].fillna(valid.median())

        return df

    def save_audit(self, path):
        out_file = Path(path)
        # make the parent folder if it doesn't exist yet
        out_file.parent.mkdir(parents=True, exist_ok=True)
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(self.audit(), f, indent=4)