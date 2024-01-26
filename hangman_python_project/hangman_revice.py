import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ['hello', 'excuse', 'supereme', 'nation', 'judiciary']
random_word = random.choice(words)
print(random_word)
lives = 6
blanks = []
for _ in range(len(random_word)):
    blanks += "_"
print(blanks)
end_of_game = False
while not end_of_game:
    user_guess = input("Guess letters in words: ")
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_guess:
            blanks[position] = letter
    if user_guess not in random_word:
        lives -= 1
        print("lives left", lives)
    if user_guess in random_word:
        print(f"{user_guess} is already prsent in {blanks}, choose another letter")

    print(f"{''.join(blanks)}")
    if "_" not in blanks:
        end_of_game = True
        print("you win")
    if lives == 0:
        end_of_game = True
        print("end of live")
    print(stages[lives])
