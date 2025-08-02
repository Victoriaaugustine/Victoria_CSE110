# Shopping Cart Program - Milestone Version
# This version allows adding and viewing items (names only)

print("Welcome to the Shopping Cart Program!")

# List to store item names
cart_items = []

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ")

    if choice == "1":
        item = input("What item would you like to add? ")
        cart_items.append(item)
        print(f"'{item}' has been added to the cart.")

    elif choice == "2":
        print("The contents of the shopping cart are:")
        for item in cart_items:
            print(item)

    elif choice == "3" or choice == "4":
        print("This feature will be available in the final version.")

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid option. Please choose between 1-5.")
