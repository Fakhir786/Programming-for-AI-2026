from pathlib import Path
from patient_dataset import PatientDataset


def main():
    root = Path(__file__).resolve().parent
    csv_path = root / "data" / "patients_messy.csv"

    ds = PatientDataset(csv_path)

    # print stats first so we can eyeball what's in the file
    stats = ds.audit()
    print("Patient Dataset Audit")
    print(f"Original rows: {stats['row_count']}")
    print(f"Exact duplicates to remove: {stats['exact_duplicate_count']}")
    print(f"Invalid age values: {stats['invalid_value_counts'].get('age', 0)}")

    df = ds.cleaned()
    print("Cleaning completed")
    print(f"Cleaned rows: {len(df)}")
    print(f"Age values imputed: {int(df['age_imputed'].sum())}")
    print(f"Heart-rate values imputed: {int(df['heart_rate_imputed'].sum())}")

    ds.save_audit(root / "output" / "audit.json")
    print("Saved: output/audit.json")

    df.to_csv(root / "output" / "patients_clean.csv", index=False)
    print("Saved: output/patients_clean.csv")


if __name__ == "__main__":
    main()