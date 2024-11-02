# Check if a string input is uppercase, lowercase, or a mix.

txt = input("Enter the String value:")

if  txt.isupper():
    print("The string is in uppercase.")
elif txt.islower():
    print("The  string is in lowercase.")
else:
    print("The string is a mix of uppercase and lowercase.")

