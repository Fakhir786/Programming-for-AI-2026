try:
    age=int(input("Enter your age:"))
except ValueError:
    print("Enter numeric value only.")
else:
    print(age)
    
    
try:     
    numerator = float(input("Numerator: "))     
    denominator = float(input("Denominator: "))     
    result = numerator / denominator 
except ValueError:     
    print("Enter numeric values only.") 
except ZeroDivisionError:     
    print("The denominator cannot be zero.") 
else:     
    print("Result:", result) 
    
