# File: word_puzzle_milestone.py
# Author: Victoria Goodnews Augustine
# Course: CSE 110 - Introduction to Programming
# Project: W04 Word Puzzle (Milestone)
#
# This is the milestone version of the Word Puzzle game.
# It includes: a secret word, user guesses, looping until correct, 
# and counting the number of guesses.
# Hints will be added in the final version.

print("Welcome to the word guessing game!")

secret_word = "mosiah"  # secret word (all lowercase)
guess = ""
guess_count = 0

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
    else:
        print("Your guess was not correct.")

print(f"It took you {guess_count} guesses.")
