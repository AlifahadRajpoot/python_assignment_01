# Use a loop to print numbers in reverse order within a given range.
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Print numbers in reverse order from end to start
for num in range(end, start - 1, -1):
    print(num, end=" ")
