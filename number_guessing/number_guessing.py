import random

lower_num, higher_num = 1, 10
random_num = random.randint(lower_num, higher_num)
# print(random_num)
print(f"Guess the number in the range of {lower_num} and {higher_num}.")

limit = 10-1
print(f"Total limit left {limit + 1}")
game_active = True
while game_active:
    try:
        user_guess = int(input("Guess: "))
    except ValueError as e:
        print("Please enter a valid number.")

    if limit == 0:
        print("Limit reached! restart the game again")
        game_active = False
    
    if user_guess > random_num:
        print("The number is lower")
        limit -= 1
    elif user_guess < random_num:
        print("The number is higher")
        limit -= 1
    
    else:
        print("You guessed it!")
        break
