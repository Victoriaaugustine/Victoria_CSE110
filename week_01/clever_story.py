# I added a second part to the story with more prompts like a place, emotion, and food to make it fun and more creative.

# Ask the user for input
print("Please enter the following:\n")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")

# Extra inputs for creativity
place = input("place: ")
emotion = input("emotion: ")
food = input("favorite food: ")

# Output the completed story
print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was t m,o {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print(f"right in front of my family.")

# Extra creative part
print(f"\nThen suddenly, it ran into the {place}, causing everyone to feel {emotion}.")
print(f"To celebrate surviving the chaos, we all sat down and ate some delicious {food}.")
print("What a day!")
