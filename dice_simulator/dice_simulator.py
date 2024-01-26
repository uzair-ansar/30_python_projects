"""
Python Project
Author: Mohammad Uzair Ansari
Description: Using python random module, list and python functions
"""

import random

def roll_dice(amount):
    if amount <= 0:
        raise ValueError
    
    rolls = []
    for i in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input = input("How many dice would you like to roll? ")

            if user_input.lower() == "exit":
                print("Thanks for playing!")
                break
            result = roll_dice(int(user_input))
            print(*result, sep=", ")
            sum_result = sum(result)
            print(f"Sum of the dice rolls: {sum_result}")
            

        except ValueError:
            print("Please provide a valid input")

if __name__ == '__main__':
    main()
