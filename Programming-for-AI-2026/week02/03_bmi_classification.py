weight=float(input('Enter you weight in KGs:'))
height=float(input('Enter your height in metres:'))
BMI=(weight/height)**2
if BMI<=18.5 and BMI>0:
  print("Underweight")
elif BMI ==0:
  print("Input Error")
elif BMI <=25 and BMI >18.5:
  print("Normal")
elif BMI >25 and BMI <30:
  print("Overweight")
else:
  print("Obese")