import datetime

# Menu with prices
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Coffee": 80,
    "Ice Cream": 100
}

order = {}  # store items and quantity

print("------ Welcome to Python Restaurant ------")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

while True:
    item = input("\nEnter item to order (or 'done' to finish): ").title()
    if item == "Done":
        break
    elif item in menu:
        qty = int(input(f"Enter quantity of {item}: "))
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        print(f"{qty} x {item} added to order ✅")
    else:
        print("❌ Item not available, try again.")

# Bill Calculation
if order:
    print("\n------ Bill Summary ------")
    subtotal = 0
    for item, qty in order.items():
        price = menu[item] * qty
        subtotal += price
        print(f"{item} x {qty} = ₹{price}")

    tax = subtotal * 0.05         # 5% GST
    discount = 0
    coupon = input("\nEnter coupon code (or press Enter to skip): ").upper()
    if coupon == "SAVE10":
        discount = subtotal * 0.10

    total = subtotal + tax - discount

    print("\nSubtotal: ₹", subtotal)
    print("GST (5%): ₹", round(tax, 2))
    print("Discount: ₹", round(discount, 2))
    print("Total Amount to Pay: ₹", round(total, 2))

    print("\nThank you for ordering! 🎉")
    print("Order Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("No items ordered.")
