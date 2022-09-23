DISCOUNT = 0.9
total_price = 0
number_of_items = int(input("Number of items: "))
for item in range(0, number_of_items, 1):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price * DISCOUNT
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
