# Use nested loops to print a pyramid pattern of *.
rows = 5

for i in range(rows):
    # Inner loop for spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Inner loop for stars
    for k in range(2 * i + 1):
        print("*", end="")
    # Move to the next line after each row
    print()
