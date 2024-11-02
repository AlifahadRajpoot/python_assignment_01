# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

num =  float(input("Enter a grade percentage: "))

if num >= 90:
    print("Your grade is A")
elif num  >= 80 and  num < 90:
    print("Your grade is B")
elif num >= 70 and  num < 80:
    print("Your grade is  C")
elif num >= 60 and  num < 70:
    print("Your grade is D")
else:
    print("Your grade is F")


