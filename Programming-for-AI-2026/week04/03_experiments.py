import json
from pathlib import Path
from experiment import Experiment


def save_experiments(experiments, file_path):
    """Save Experiment objects to a Json File"""
    json_path = Path(file_path)

    json_path.parent.mkdir(parents=True, exist_ok=True)
    experiment_records = []

    for experiment in experiments:
        experiment_records.append(experiment.to.disctionary())
    with json_path.open("w", encoding="utf-8") as file:
        json.dump(experiment_records, file, indent=4)


def load_experiments(file_path):
    """Load and return experiment dictionaries from a JSON file."""
    json_path = Path(file_path)
    with json_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    """Create ,save,load,and compare AI experiments"""
    lab_folder = Path(__file__).resolve().parent
    json_path = lab_folder / "data" / "experiments.json"

    experiments = [
        Experiment("EXP_001", "LogisticRegression", "Student Performance", 0.84),
        Experiment("EXP_002", "Decision Tree", "Student Performance", 0.88),
        Experiment("EXP_003", "K-NEAREST NEIGHBOURS", "Student Performance", 0.91),
    ]
    save_experiments(experiments, json_path)
    print("Experiments saved at :", json_path.resolve())
    loaded_experiments = load_experiments(json_path)

    print("Loaded experiments:")

    for experiment in loaded_experiments:
        print(experiment)

    best_experiment = loaded_experiments[0]

    for experiment in loaded_experiments:
        if experiment["accuracy"] > best_experiment["accuracy"]:
            best_experiment = experiment

    print()
    print("Best Experiment:")
    print(best_experiment)


if __name__ == "__main__":
    main()
