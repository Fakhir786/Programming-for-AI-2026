from student_utils import calculate_average, calculate_grade, format_summary


assert calculate_average([78, 65, 92]) == 78.33333333333333
assert calculate_average([0, 50, 85, 100]) == 58.75

assert calculate_grade(85) == "A"
assert calculate_grade(70) == "B"
assert calculate_grade(50) == "D"

assert format_summary("Huraira", 78.5, "B") == "Huraira takes B grade which makes average:78.5"

print("All tests passed!")