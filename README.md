# Hangman Game

A classic command-line Hangman game written in Python. Guess the hidden word one letter at a time before you run out of wrong guesses.

## Features

- Randomly selects a word from a predefined word list
- Displays the word progress as underscores, revealing correctly guessed letters
- Tracks and displays remaining wrong guesses
- Validates input (single alphabetic character only)
- Prevents guessing the same letter twice
- Announces win/loss with the correct word at the end

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library `random` module)

## Usage

Run the script from the command line:

```bash
python hangman.py
```

Example session:

```
=================================
      WELCOME TO HANGMAN
=================================

Word: _ _ _ _ _ _
Wrong Guesses Left: 6
Enter a letter: a
Correct Guess!

Word: a _ _ _ _ _
Wrong Guesses Left: 6
Enter a letter: z
Wrong Guess!

Word: a _ _ _ _ _
Wrong Guesses Left: 5
Enter a letter: p
Correct Guess!
...
Congratulations!
You guessed the word: apple
```

## Word List

The word is randomly chosen from:

```
python, computer, flower, school, apple
```

## Rules

- You have **6 wrong guesses** before the game ends.
- Enter one letter at a time; only single alphabetic characters are accepted.
- Guessing the same letter twice doesn't cost you a turn.
- The game ends when either:
  - You reveal the entire word (win), or
  - You run out of wrong guesses (lose — the correct word is revealed).

## Project Structure

```
hangman.py   # Full game logic: word selection, game loop, input validation, win/loss handling
```

## Notes / Limitations

- The word list is short and hardcoded; edit the `words` list in the script to add more words.
- No score tracking or replay prompt — the script runs once per execution.
- No visual hangman drawing (ASCII art) is included; progress is shown via letters guessed and guesses remaining.
