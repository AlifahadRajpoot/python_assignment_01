# Write a program that breaks the loop when a certain condition is met.
while True:
    user_input = int(input("Enter a number: "))
    if user_input < 0:
        print("Negitive number is not allowed")
        break
    else:
        print("You entered a positive number")
    