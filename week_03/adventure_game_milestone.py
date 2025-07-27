# adventure_game_milestone.py
# Milestone Version: Implements the first question and choices only

def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You are an explorer standing at the entrance of a mysterious CAVE.")
    print("You see three items in front of you: a TORCH, a SWORD, and a ROPE.")
    first_choice = input("Which one do you want to pick up? (TORCH / SWORD / ROPE): ").strip().lower()

    if first_choice == "torch":
        print("\nYou pick up the torch and light it. The cave ahead is dark but now visible.")
        # Further choices to be implemented in final version

    elif first_choice == "sword":
        print("\nYou grip the sword and enter the cave bravely.")
        # Further choices to be implemented in final version

    elif first_choice == "rope":
        print("\nYou take the rope. Useful for climbing, maybe?")
        # Further choices to be implemented in final version

    else:
        print("Invalid item. Please choose TORCH, SWORD, or ROPE. Start over.")

# Start the game
adventure_game()
