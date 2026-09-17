from student_utils import calculate_grade,calculate_average,format_summary

name="Ali"
marks=[78,60,78]
average=calculate_average(marks)
grade=calculate_grade(average)

summary=format_summary(name,average,grade)
print(summary)