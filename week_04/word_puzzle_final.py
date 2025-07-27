# CSE 110 - Word Puzzle Game (Final Version)
# Full game with hints and guess checking

print("Welcome to the word guessing game!")

secret_word = "mosiah"
word_length = len(secret_word)
guess_count = 0
guessed_correctly = False

while not guessed_correctly:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if len(guess) != word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue  # Don't give a hint, but count the guess

    if guess == secret_word:
        guessed_correctly = True
    else:
        # Generate hint
        hint = ""
        for i in range(word_length):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint += guess[i].lower() + " "
            else:
                hint += "_ "
        print("Your hint is:", hint.strip())

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
