
# G1. Missing colon

# Error: Missing colon after the function definition.
# Cause: Python function definitions must end with a colon.
# Fix: Add a colon after def average(a, b).

def average(a, b):
    return (a + b) / 2

print("G1:", average(10, 20))


# G2. Returning printed output

# Error: The function returns None instead of the doubled value.
# Cause: print() displays a value but returns None.
# Fix: Return number * 2 directly.

def double(number):
    return number * 2

print("G2:", double(5))


# G3. Silent failure

# Error: The program silently ignores invalid age input.
# Cause: The except block uses pass, so the error is not reported.
# Fix: Catch ValueError and tell the user to enter a valid number.

try:
    age = int(input("Age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid number for age.")


# G4. Refactoring challenge

# Error: The grade logic is repeated for every student.
# Cause: The same if/elif/else code is written multiple times.
# Fix: Create one calculate_grade() function and reuse it.

def calculate_grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 70:
        return "B"
    else:
        return "below B"


ali_mark = 88
sara_mark = 73
hamza_mark = 62

print("Ali:", calculate_grade(ali_mark))
print("Sara:", calculate_grade(sara_mark))
print("Hamza:", calculate_grade(hamza_mark))
