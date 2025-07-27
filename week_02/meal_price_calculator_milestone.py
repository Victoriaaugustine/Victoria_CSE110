# meal_price_calculator_milestone.py
# Milestone Submission for W02 Project
# This version calculates only the subtotal (no tax, payment, or change)

# Ask for meal prices
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask for quantity
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Display subtotal
print(f"\nSubtotal: ${subtotal:.2f}")