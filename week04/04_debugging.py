import csv
import json

# F1
# Error: self is missing
# Cause: self is required in the constructor
# Fix: Add self as the first parameter


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student = Student("Ali", [85, 90])

print(student.name)
print(student.marks)


# F2
# Error: File is opened in read mode
# Cause: Read mode cannot write data
# Fix: Change "r" to "w"

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ali", 85])


# F3
# Error: Python object cannot be directly saved as JSON
# Cause: JSON needs JSON-compatible data
# Fix: Convert the object to a dictionary first

model = {"name": "Student Model", "accuracy": 0.92}

with open("model.json", "w", encoding="utf-8") as file:
    json.dump(model, file, indent=4)

print("Model saved successfully")
