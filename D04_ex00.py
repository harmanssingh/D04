#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

rand_num = random.randint(1, 25)

for count in range(5):
    try:
        user_inp = int(input("Guess the number: "))
        if user_inp == rand_num:
            print("Great! You guessed it right")
            break
        elif user_inp > rand_num and user_inp <= 25:
            print("Too high")
            continue
        elif user_inp < rand_num and user_inp > 0:
            print("Too low")
            continue
        else:
            print("Number not in the range of 1 to 25")
            continue
    except:
            print("Nice try, enter a number")
            continue
else:
    print("You have exceeded the maximum trials allowed. Better luck next time.")


################################################################################
def main():


    print("") # Remove this and replace with your function calls


if __name__ == '__main__':
    main()
