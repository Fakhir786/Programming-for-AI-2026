from student_toolkit import parse_marks,generate_summary,save_report
name = input("Enter student name: ")
marks_text = input("Enter marks separated by commas: ")

try:
    marks = parse_marks(marks_text)

    report = generate_summary(name, marks)

    print("\n" + report)

    save_report("student_report.txt", report)

    print("\nReport saved to student_report.txt")

except ValueError as error:
    print("Invalid marks:", error)