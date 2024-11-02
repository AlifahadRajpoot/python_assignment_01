# Use a loop to count the number of digits in an integer.

num = int(input("Enter the number:"))
count = 0
while num != 0:
    count += 1
    num = num // 10    #yaha par 10 par divide karna sa ya end wala digit ko remove karda ga or  count ko 1 increment karda ga asa he loop har digit par chala ga jab tak wo 0 ni ho jata or phir end par hum ko digits jo ka count ma store han wo return ho ga 

print("Number of digits:", count)