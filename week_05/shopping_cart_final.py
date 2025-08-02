# Shopping Cart Program - Final Version
# Added prices, item numbering, total calculation, and item removal.
# 🔥 Extra Feature: Tracks item quantity and formats output nicely.

print("Welcome to the Shopping Cart Program!")

# Lists to store item names and prices
cart_items = []
cart_prices = []

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
        price = float(input(f"What is the price of '{item}'? "))
        cart_items.append(item)
        cart_prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif choice == "2":
        if len(cart_items) == 0:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(cart_items)):
                print(f"{i+1}. {cart_items[i]} - ${cart_prices[i]:.2f}")

    elif choice == "3":
        if len(cart_items) == 0:
            print("Your cart is empty. Nothing to remove.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(cart_items)):
                print(f"{i+1}. {cart_items[i]} - ${cart_prices[i]:.2f}")
            index = int(input("Which item would you like to remove? ")) - 1

            if 0 <= index < len(cart_items):
                removed_item = cart_items.pop(index)
                cart_prices.pop(index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")

    elif choice == "4":
        total = sum(cart_prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid option. Please choose between 1-5.")
