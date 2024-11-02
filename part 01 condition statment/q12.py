#  Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
temp = int(input("Enter the temperature in Celsius:"))

if temp <= 0:
    print("It's freezing!")
elif temp <= 25 and temp  > 0:
    print("It's moderate!")
else:
    print("It's hot!")

