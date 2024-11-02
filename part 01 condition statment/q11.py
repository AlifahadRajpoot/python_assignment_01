# Check if a given number is a multiple of both 3 and 5.

n = int(input("Enter the number:"))

if n %  3 == 0 and n % 5 == 0:
    print(n,"is a multiple of both 3 and 5")
else:
    print(n,"is not a multiple of both 3 and 5")
