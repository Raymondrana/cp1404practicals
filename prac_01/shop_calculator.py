"""
shop_calculator.py
Calculates the total price for a number of items and applies a discount if applicable.
"""

number_of_items = int(input("Number of items: "))

total_price = 0.0

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# 10% discount if total price is over $100
if total_price > 100:
    total_price *= 0.90

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
