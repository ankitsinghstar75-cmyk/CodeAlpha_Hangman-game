import random

# Predefined list of words
words = ["python", "computer", "flower", "school", "apple"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display word with underscores
display = ["_"] * len(word)

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong Guesses Left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check guessed letter
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong Guess!")

# Final Result
if "_" not in display:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word
  
