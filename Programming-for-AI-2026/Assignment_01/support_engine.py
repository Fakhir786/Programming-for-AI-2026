"""Student Support Rule Engine.

Reads a student's attendance, assignment average, and missed submissions,
classifies the student into a support-priority category, and displays an
advisory message.
"""


def read_float(prompt, minimum, maximum):
    """Read and return a valid floating-point value."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Value must be between {minimum} and {maximum}.")


def read_int(prompt, minimum):
    """Read and return a valid integer value."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value >= minimum:
            return value

        print(f"Value must be at least {minimum}.")


def classify_support(attendance, assignment_average, missed_submissions):
    """Return the student support-priority category."""
    if attendance < 60 or missed_submissions >= 4:
        return "High priority"

    if attendance < 75 or assignment_average < 60 or missed_submissions >= 2:
        return "Moderate priority"

    return "Routine monitoring"


def format_message(category):
    """Return an advisory message for the category."""
    messages = {
        "High priority": "Immediate academic support is recommended.",
        "Moderate priority": "Monitor progress and provide targeted guidance.",
        "Routine monitoring": "Continue routine monitoring.",
    }
    return messages.get(category, "Unknown support category.")


def main():
    """Run the student support rule engine."""
    print("Student Support Rule Engine")
    print("----------------------------")

    attendance = read_float("Attendance percentage: ", 0, 100)
    assignment_average = read_float("Assignment average: ", 0, 100)
    missed_submissions = read_int("Missed submissions: ", 0)

    category = classify_support(attendance, assignment_average, missed_submissions)
    message = format_message(category)

    print()
    print(f"Support category: {category}")
    print(f"Advisory: {message}")


if __name__ == "__main__":
    main()