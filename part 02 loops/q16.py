# Create a program to calculate the sum of the digits of an inputted integer.
num = int(input("Enter the number:"))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10
print("Sum of the digits is:", sum_of_digits)
    
    
# work flow of code:

# num = 123, sum_of_digits = 0

# First iteration:
# digit = 123 % 10 → 3

# sum_of_digits = 0 + 3 → 3
# num = 123 // 10 → 12
# Second iteration:
# digit = 12 % 10 → 2

# sum_of_digits = 3 + 2 → 5
# num = 12 // 10 → 1

# Third iteration:
# digit = 1 % 10 → 1

# sum_of_digits = 5 + 1 → 6
# num = 1 // 10 → 0

# The loop ends, and it prints: Sum of the digits is: 6.
# So, the sum of the digits of 123 is 6.