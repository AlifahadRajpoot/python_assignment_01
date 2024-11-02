# Create a program that simulates a countdown timer starting from a given number down to zero.

# Input: countdown starting number
countdown_start = int(input("Enter the starting number for the countdown: "))

# Countdown loop
while countdown_start >= 0:
    print(countdown_start)
    countdown_start -= 1

print("Countdown finished!")
