import csv
from pathlib import Path
from student import Student


def load_students(file_path):
    students = []

    with Path(file_path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            marks = [float(row["mark1"]), float(row["mark2"]), float(row["mark3"])]

            students.append(Student(row["sap_id"], row["name"], marks))

    return students


def save_student_report(student, file_path):
    report = f"""SAP ID: {student.sap_id}
Student Name: {student.name}
Average: {student.calculate_average():.2f}
Grade: {student.calculate_grade()}
"""

    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    with Path(file_path).open("w", encoding="utf-8") as file:
        file.write(report)


def main():
    try:
        students = load_students("week04/data/students.csv")

        for student in students:
            print(student.format_profile())
            print()

        total = 0

        for student in students:
            total += student.calculate_average()

        class_average = total / len(students)

        print(f"Class Average: {class_average:.2f}")
        print()

        report_paths = []

        for student in students:
            report_path = Path("week04/reports") / f"{student.sap_id}.txt"
            save_student_report(student, report_path)
            report_paths.append(report_path)

        print("Saved Reports:")
        for report_path in report_paths:
            print(report_path)

        print()

        print("Report Contents:")
        for report_path in report_paths:
            with report_path.open("r", encoding="utf-8") as file:
                print(file.read())

    except FileNotFoundError:
        print("Student data file was not found in week04/data.")

    except ValueError as error:
        print(f"Invalid student data: {error}")


if __name__ == "__main__":
    main()
