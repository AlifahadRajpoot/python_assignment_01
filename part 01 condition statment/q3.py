#  Write a program that checks if a given year is a leap year.

year = int(input("Enter the Year:"))

if year % 4 == 0 and year % 100 != 0  or year % 400 == 0:
    print(year ,  "is a leap year")
else:
    print(year ,  "is not a leap year")




    
