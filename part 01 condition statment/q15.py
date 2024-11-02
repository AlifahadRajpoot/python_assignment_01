#  Write a program to check if a number is within a specified range

num = int(input("Enter the number:"))
lower_limit = int(input("Enter the lower limit:"))
upper_limit = int(input("Enter the upper limit:"))
if lower_limit <= num <= upper_limit:
    print(num,"is within the specified range.")
else:
    print(num,"is not within the specified range.")