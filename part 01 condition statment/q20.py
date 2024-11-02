# create a program that evaluates if an inputted number is prime.

n = int(input("Enter the number you want to check: "))

if n <= 1:
    print(n, "is not a prime number")
elif n <= 3:
    print(n, "is a prime number")  
elif n % 2 == 0 or n % 3 == 0:
    print(n, "is not a prime number")
else:
    
    is_prime = True
    if n % 5 == 0:
        is_prime = False
    elif n % 7 == 0:
        is_prime = False
    elif n % 11 == 0:
        is_prime = False
    elif n % 13 == 0:
        is_prime = False
    elif n % 17 == 0:
        is_prime = False
    elif n % 19 == 0:
        is_prime = False
    elif n % 23 == 0:
        is_prime = False
    elif n % 29 == 0:
        is_prime = False
    elif n % 31 == 0:
        is_prime = False
    elif n % 37 == 0:
        is_prime = False
    elif n % 41 == 0:
        is_prime = False
    elif n % 43 == 0:
        is_prime = False
    elif n % 47 == 0:
        is_prime = False

    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")



