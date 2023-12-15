DISCOUNT = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
price_of_all_items = float(0)
for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    price_of_all_items += price_of_item
if price_of_all_items > 100:
    price_of_all_items = price_of_all_items * (1-DISCOUNT)
print(f"The total price for {number_of_items} items is ${price_of_all_items:.2f}")
