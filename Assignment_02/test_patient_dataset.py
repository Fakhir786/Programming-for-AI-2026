from pathlib import Path
import json
from patient_dataset import PatientDataset

def test_suite():

    root = Path(__file__).resolve().parent
    csv_file = root / "data" / "patients_messy.csv"

    try:
        ds = PatientDataset(csv_file)
        ds.validate_required(["patient_id", "bad_col"])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    ds = PatientDataset(csv_file)
    res = ds.audit()
    assert res["row_count"] == 100
    assert res["exact_duplicate_count"] == 1

    cleaned = ds.cleaned()
    assert len(cleaned) == 99

    assert cleaned["age"].between(0, 120).all()
    assert cleaned["heart_rate"].between(30, 220).all()

    assert int(cleaned["age_imputed"].sum()) == 11
    assert int(cleaned["heart_rate_imputed"].sum()) == 9

    value = root / "data" / "temp_bad.csv"
    value.write_text("patient_id, age, heart_rate, department\nP1, 30, 70, Cardio\nP1, 40, 80, Neuro")
    try:
        PatientDataset(value).cleaned()
        value.unlink()
        assert False, "Should have raised ValueError on conflict"
    except ValueError:
        if value.exists():
            value.unlink()

    orig_shape = ds.raw.shape
    _ = ds.audit()
    _ = ds.cleaned()
    assert ds.raw.shape == orig_shape

    ind_df = ds.cleaned()
    ind_df.loc[0, "age"] = 999
    assert ds.raw.loc[0, "age"] != 999

    json_path = root / "output" / "audit.json"
    ds.save_audit(json_path)
    with open(json_path, "r", encoding = "utf-8") as f:
        data = json.load(f)
    assert data["row_count"] == 100

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_suite()
