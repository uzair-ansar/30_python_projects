from random import choice 

def run_game():
    user_word = choice(["banana", "apple", "coin", "loop"])

    username = input("What is your name? ")
    print(f"Welcome to hangman, {username}")

    guess_word = ""
    tries = 3

    while tries > 0:
        blanks = 0
        print("Word: ", end="")

        for char in user_word:
            if char in guess_word:
                print(char, end="")

            else:
                print("_", end="")
                blanks += 1
        print()

        if blanks == 0:
            print("You got it!")
            break

        guess = input("Enter a letter: ")

        if guess in guess_word:
            print(f"You already used: '{guess}. Please enter another letter")
            continue

        guess_word += guess

        if guess not in user_word:
            tries -= 1
            print(f"Sorry, that was wrong...({tries} tries remainig)")

            if tries == 0:
                print("No more tries remainig...You lose.")
                break

if __name__ == '__main__':
    run_game()
