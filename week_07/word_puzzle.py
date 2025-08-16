# File: word_puzzle.py
# Author: Victoria Goodnews Augustine
# Course: CSE 110 - Introduction to Programming
# Project: W04 Word Puzzle (Final Version)
#
# This is the completed version of the Word Puzzle game.
# Features:
# - Checks guess length
# - Provides hints (underscores, lowercase for wrong spot, uppercase for correct spot)
# - Counts guesses
# - Creativity: Randomly selects a secret word from a list

import random

print("Welcome to the word guessing game!")

# Choose a random word from a list for creativity
words = ["mosiah", "temple", "nephi", "helaman", "moroni"]
secret_word = random.choice(words)

# Initial hint (all underscores)
hint = ["_"] * len(secret_word)
print("Your hint is:", " ".join(hint))

guess_count = 0
guess = ""

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check length first
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    # Generate the hint
    hint = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint.append(guess[i].upper())  # correct letter in correct position
        elif guess[i] in secret_word:
            hint.append(guess[i].lower())  # letter exists but wrong position
        else:
            hint.append("_")  # letter not in the word

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        break
    else:
        print("Your hint is:", " ".join(hint))

print(f"It took you {guess_count} guesses.")
