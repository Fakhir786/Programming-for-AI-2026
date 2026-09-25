class Student:
    def __init__(self, sap_id, name, marks):
        self.sap_id = sap_id
        self.name = name
        self.set_marks(marks)

    def set_marks(self, marks):
        if len(marks) == 0:
            raise ValueError("Marks list cannot be empty")

        for mark in marks:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")

        self._marks = marks.copy()

    def get_marks(self):
        return self._marks.copy()

    def calculate_average(self):
        return sum(self._marks) / len(self._marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 85:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def format_profile(self):
        average = self.calculate_average()
        grade = self.calculate_grade()

        return f"SAP ID: {self.sap_id}\nName: {self.name}\nMarks: {self._marks}\nAverage: {average:.2f}\nGrade: {grade}"


student1 = Student("23F-001", "Fakhir", [78, 86, 91])
student2 = Student("23F-002", "Ali", [0, 100])
student3 = Student("23F-003", "Sara", [65, 72, 88])

print(student1.format_profile())
print()
print(student2.format_profile())
print()
print(student3.format_profile())


marks_copy = student1.get_marks()
marks_copy[0] = 100

print("Changed copy:", marks_copy)
print("Original marks:", student1.get_marks())


try:
    student4 = Student("23F-004", "Test", [])
except ValueError as e:
    print("Error:", e)


try:
    student5 = Student("23F-005", "Test", [72, 105])
except ValueError as e:
    print("Error:", e)