# CSE 110 - Word Puzzle Game (Milestone)
# Basic version with guess loop and count

print("Welcome to the word guessing game!")

secret_word = "mosiah"
guess = ""
guess_count = 0

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess != secret_word:
        print("Your guess was not correct.")

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
