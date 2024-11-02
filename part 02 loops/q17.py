# . Write a program that continues to ask for a number until the correct number is guessed.
num = 42
while True:
    guess = int(input("Guess the number:"))
    if  guess == num:
        print("You guessed it!")
        break
    else:
        print("Try again!")
