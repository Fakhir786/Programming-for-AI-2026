import json
from pathlib import Path
from experiment import Experiment


lab_folder = Path(__file__).resolve().parent
json_path = lab_folder / "data" / "experiments.json"
report_path = lab_folder / "reports" / "experiment_summary.txt"


def add_experiment(experiments, experiment_id, model_name, dataset_name, accuracy):
    """Create, validate, and add an experiment."""

    try:
        accuracy = float(accuracy)
    except ValueError:
        raise ValueError("Accuracy must be a number.")

    experiment = Experiment(experiment_id, model_name, dataset_name, accuracy)

    experiments.append(experiment)
    return experiment


def display_experiments(experiments):
    """Display all experiments clearly."""

    if not experiments:
        print("No experiments are available.")
        return

    for experiment in experiments:
        print(
            f"{experiment.experiment_id} | "
            f"{experiment.model_name} | "
            f"{experiment.dataset_name} | "
            f"Accuracy: {experiment.accuracy:.2f}"
        )


def search_experiment(experiments, experiment_id):
    """Return an experiment with the given id."""

    for experiment in experiments:
        if experiment.experiment_id == experiment_id:
            return experiment

    return None


def find_best_experiment(experiments):
    if not experiments:
        return None

    return max(experiments, key=lambda experiment: experiment.accuracy)


def save_experiments(experiments, file_path):
    """Save Experiment objects to a JSON file."""

    json_path = Path(file_path)

    json_path.parent.mkdir(parents=True, exist_ok=True)

    records = [experiment.to_dictionary() for experiment in experiments]

    try:
        with json_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    except PermissionError:
        print(f"The location is not writable: {json_path}")


def load_experiments(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        experiments = []

        for record in records:
            experiment = Experiment(
                record["experiment_id"],
                record["model_name"],
                record["dataset_name"],
                record["accuracy"],
            )

            experiments.append(experiment)

        return experiments

    except json.JSONDecodeError:
        print("The JSON data is invalid.")
        return []


def write_summary(experiments, file_path):
    file_path = Path(file_path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    best_experiment = find_best_experiment(experiments)

    lines = []

    for experiment in experiments:
        lines.append(
            f"{experiment.experiment_id} | "
            f"{experiment.model_name} | "
            f"Accuracy: {experiment.accuracy}"
        )

    if best_experiment is not None:
        lines.append("")
        lines.append("Best Experiment:")
        lines.append(
            f"{best_experiment.experiment_id} | "
            f"{best_experiment.model_name} | "
            f"Accuracy: {best_experiment.accuracy}"
        )

    try:
        with file_path.open("w", encoding="utf-8") as file:
            file.write("\n".join(lines))

    except PermissionError:
        print(f"The location is not writable: {file_path}")


def run_assertions():
    experiments = []

    experiment = add_experiment(
        experiments, "EXP-001", "Decision Tree", "Student Performance", "0.88"
    )

    assert experiment.accuracy == 0.88
    assert experiment.to_dictionary()["model_name"] == "Decision Tree"

    found = search_experiment(experiments, "EXP-001")
    assert found is experiment

    not_found = search_experiment(experiments, "EXP-999")
    assert not_found is None

    add_experiment(experiments, "EXP-002", "kNN", "Student Performance", 0.91)

    best = find_best_experiment(experiments)
    assert best.experiment_id == "EXP-002"

    try:
        Experiment("EXP-003", "Test Model", "Test Dataset", 1.5)
        assert False
    except ValueError:
        pass


def main():
    run_assertions()

    experiments = load_experiments(json_path)

    print("Records loaded at startup:", len(experiments))
    print()

    if len(experiments) == 0:
        add_experiment(
            experiments, "EXP-001", "Logistic Regression", "Student Performance", 0.84
        )

        add_experiment(
            experiments, "EXP-002", "Decision Tree", "Student Performance", 0.88
        )

        add_experiment(experiments, "EXP-003", "kNN", "Student Performance", 0.91)

    print("All Experiments:")
    display_experiments(experiments)
    print()

    found = search_experiment(experiments, "EXP-002")

    if found is not None:
        print("EXP-002:")
        print(found.to_dictionary())
    else:
        print("Experiment was not found.")

    print()

    best = find_best_experiment(experiments)

    if best is not None:
        print("Best Experiment:")
        print(best.to_dictionary())

    print()

    save_experiments(experiments, json_path)

    write_summary(experiments, report_path)

    reloaded_experiments = load_experiments(json_path)

    print("Successfully reloaded records:", len(reloaded_experiments))

    assert len(reloaded_experiments) == len(experiments)


if __name__ == "__main__":
    main()
