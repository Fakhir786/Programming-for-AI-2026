marks=[78,65,92,85,48,91]
passing_marks=[x for x in marks if x>=50]
fail_marks=[i for i in marks if i<50]
sum=0
for i in marks:
  sum+=i
print(f"Average= {sum/len(marks)}")
max=marks[0]
min=marks[0]
for i in marks:
  if i>max:
    max=i
  if i<min:
    min=i
print(f"Max: {max}")
print(f"Min: {min}")
print(f"Passing: {passing_marks}")
print(f"Failing: {fail_marks}")