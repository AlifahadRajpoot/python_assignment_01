#  Check if a year input by the user is a century year.

year = int(input("Enter the Year:"))

if  year % 100 == 0 and  year % 400 == 0:
    print(year ,"is a leap century year") 
elif year % 100 ==0:
    print(year ,"is a century year")
else:
    print(year ,"is not a century year")


        





