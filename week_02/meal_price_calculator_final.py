# meal_price_calculator_final.py
# Final Submission for W02 Project - Meal Price Calculator
# Creativity Added: This version includes drink cost per person and a tip percentage.

# Ask for meal prices
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask for quantity
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Ask if drinks are included
drink_price = float(input("What is the price of a drink per person? "))

# Calculate subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults) + (drink_price * (num_children + num_adults))
print(f"\nSubtotal: ${subtotal:.2f}")

# Ask for sales tax
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Compute total
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# Tip (optional creativity)
tip_percentage = float(input("\nWhat tip percentage would you like to give? "))
tip_amount = total * (tip_percentage / 100)
print(f"Tip: ${tip_amount:.2f}")

# Grand total with tip
grand_total = total + tip_amount
print(f"Grand Total (including tip): ${grand_total:.2f}")

# Ask for payment
payment = float(input("\nWhat is the payment amount? "))
change = payment - grand_total
print(f"Change: ${change:.2f}")