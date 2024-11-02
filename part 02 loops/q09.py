#  Write a program to print the first 10 Fibonacci numbers.

n_terms = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n_terms):  #yaha paar _ loop ka ander use ni ho gi ya bs output ko ak readable form ma convert kar da gi yani space da ga hara  number ke baad

    print(a,end="")   #yaha par end ="" ais lia use kia ha taka number ak row ki form ma print ho agar ya na hota to number columns ki form ma print  ho jata
    a, b = b, a + b

# Placeholders are used in loops when the loop variable isn’t needed within the loop body. 
# For example, _ is often used as a placeholder to indicate that the variable is just a counter and won’t be used.

# Output before using placeholder:
# 0112358132134

# Output after using placeholder:
# 0 1 1 2 3 5 8 13 21 34 55