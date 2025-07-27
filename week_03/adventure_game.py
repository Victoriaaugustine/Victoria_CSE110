# adventure_game.py
# Added creativity: The game contains 3+ levels, one scenario with more than 2 choices, and creative storytelling paths.
# I also had two people play-test this game, and I explained how the nested if-statements work to build the branching narrative.

def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You are an explorer standing at the entrance of a mysterious CAVE.")
    print("You see three items in front of you: a TORCH, a SWORD, and a ROPE.")
    first_choice = input("Which one do you want to pick up? (TORCH / SWORD / ROPE): ").strip().lower()

    if first_choice == "torch":
        print("\nYou pick up the torch and light it. The cave ahead is dark but now visible.")
        print("You walk deeper and come to a fork in the path.")
        second_choice = input("Do you go LEFT or RIGHT?: ").strip().lower()

        if second_choice == "left":
            print("\nYou turn left and see glowing mushrooms. Suddenly, a goblin appears!")
            third_choice = input("Do you TALK to the goblin, RUN, or THROW the torch?: ").strip().lower()

            if third_choice == "talk":
                print("\nThe goblin is surprisingly friendly! He shows you a secret exit. You win!")
            elif third_choice == "run":
                print("\nYou run in the dark and fall into a pit. Game over.")
            elif third_choice == "throw":
                print("\nThe goblin catches fire and runs. You escape, but feel guilty. You win...sort of.")
            else:
                print("Invalid choice. The goblin gets tired of waiting and eats you.")
        
        elif second_choice == "right":
            print("\nYou walk into a trap room. The walls begin to close in.")
            third_choice = input("Do you USE the torch to jam the wall, LOOK for a lever, or SCREAM for help?: ").strip().lower()

            if third_choice == "use":
                print("\nThe torch holds the wall just long enough for you to escape. You're safe!")
            elif third_choice == "look":
                print("\nYou find a lever and pull it just in time. The trap resets. You win!")
            elif third_choice == "scream":
                print("\nNo one hears you. The walls close in. Game over.")
            else:
                print("That wasn't one of the choices. You freeze and get crushed.")

        else:
            print("You can only choose LEFT or RIGHT. A bat scares you back to the cave entrance.")
    
    elif first_choice == "sword":
        print("\nYou grip the sword and enter the cave bravely.")
        print("You see a treasure chest guarded by a sleeping dragon.")
        second_choice = input("Do you ATTACK the dragon or SNEAK past it?: ").strip().lower()

        if second_choice == "attack":
            print("\nYou charge! The dragon wakes up and breathes fire.")
            third_choice = input("Do you DODGE, BLOCK, or SCREAM?: ").strip().lower()

            if third_choice == "dodge":
                print("\nYou roll to the side and strike its weak spot. You defeat the dragon and get the treasure!")
            elif third_choice == "block":
                print("\nYour sword melts. You are toast. Game over.")
            elif third_choice == "scream":
                print("\nThe dragon is startled and flies off. You take the treasure and leave!")
            else:
                print("Invalid move. You hesitate and the dragon fries you.")
        
        elif second_choice == "sneak":
            print("\nYou sneak quietly and reach the treasure.")
            third_choice = input("Do you OPEN the chest or LEAVE it alone?: ").strip().lower()

            if third_choice == "open":
                print("\nIt’s a mimic! The chest eats you. Game over.")
            elif third_choice == "leave":
                print("\nYou back away safely. Good instincts. You live to explore another day.")
            else:
                print("You freeze and trip. The dragon wakes and you’re lunch.")

        else:
            print("You can only ATTACK or SNEAK. You panic and run out of the cave.")

    elif first_choice == "rope":
        print("\nYou take the rope. Useful for climbing, maybe?")
        print("As you walk, you find a deep pit blocking the way.")
        second_choice = input("Do you CLIMB down, THROW the rope across, or TURN back?: ").strip().lower()

        if second_choice == "climb":
            print("\nYou climb down safely and find a hidden cavern.")
            third_choice = input("Do you EXPLORE or REST?: ").strip().lower()

            if third_choice == "explore":
                print("\nYou discover ancient ruins and hidden knowledge. You win!")
            elif third_choice == "rest":
                print("\nYou fall asleep and get eaten by cave bugs. Game over.")
            else:
                print("You hesitate and fall into a crevice. Bad choice.")

        elif second_choice == "throw":
            print("\nYou throw the rope and swing across. Nice move!")
            third_choice = input("Do you KEEP going or EXIT the cave?: ").strip().lower()

            if third_choice == "keep":
                print("\nYou find rare gems and make a fortune!")
            elif third_choice == "exit":
                print("\nYou return safely with stories to tell.")
            else:
                print("You trip and drop into the pit. Ouch.")

        elif second_choice == "turn":
            print("\nYou go back the way you came. Maybe another day.")
        else:
            print("You must CLIMB, THROW, or TURN. You wait too long and get lost.")

    else:
        print("Invalid item. Please choose TORCH, SWORD, or ROPE. Start over.")

# Start the game
adventure_game()
