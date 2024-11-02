# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

n = int(input("Enter the number:"))

if n %  2 == 0 and n % 3 == 0:
    print(n,"is divisible of both 2 and 3")
elif n % 2 ==0:
    print(n ,"is a divisible of 2")
elif n % 3 == 0:
    print(n ,"is a divisible of 3")
else:
    print(n,"is not divisible of both 2 and 3")
