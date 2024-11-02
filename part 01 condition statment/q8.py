# Create a program that checks if a given string is a palindrome.

a = input("Enter the String:")

if a == a[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")