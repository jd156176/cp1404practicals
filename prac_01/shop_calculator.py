""" Week 1 Extension Prac, Shop Calculator"""

DISCOUNT = 0.1
THRESHOLD = 100


number_of_items = int(input("Number of Items: "))
total_price = 0

while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))

for i in range (number_of_items):
    item_price = float(input("Price of Item: "))
    total_price = total_price + item_price

if total_price > THRESHOLD:
    total_price = total_price - (total_price * DISCOUNT)

print(f"Total Price for {number_of_items} items is ${total_price:.2f}")