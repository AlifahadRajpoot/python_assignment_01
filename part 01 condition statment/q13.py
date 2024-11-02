# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
operator = input("Enter your operator (+, -, *, /):")

if  operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator. Please enter one of the following: +, -, *, /")


