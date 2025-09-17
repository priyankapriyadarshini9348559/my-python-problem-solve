print("welcome to PYTHON restaurant ")

menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}

for item, price in menu.items():
    print(f"{item}: RS{price}")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available!")

another_order = input("Do you want to order something? (yes/no): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount you have to pay is {order_total}")
