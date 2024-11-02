#  Print the sum of even and odd numbers separately up to a given number.
limit = int(input("Enter the limit of number:"))
even_sum = 0
odd_sum = 0
for i in range(1,limit+1):
    if i%2==0:
        even_sum += i
    else:
        odd_sum += i
print("Even  numbers sum:",even_sum)
print("Odd  numbers sum:",odd_sum)
