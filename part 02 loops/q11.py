#  Print the reverse of a given number.
num = int(input("Enter the number:"))
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = (reverse_num * 10) + digit
    num = num // 10
print("Reverse  of the number is:", reverse_num)
