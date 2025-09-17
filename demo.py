menu={
    'pizza':40,
    'pasta':50,
    'Burger':60,
    'salad':70,
    'coffee':80,


}
print("welcome to PYTHON resturant ")
print("pizza:RS40\npasta:RS50\nBurger:RS60\nsalad:RS70\ncoffee:RS80")
order_total=0
item_1=input("enter the name of the item you want to order= ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order ")
else:
    print(f"order item {item_1} is not available yet")

another_item=input("do you want to order something?(yes/no)")
if another_item=="yes":
    item_2=input("enter the name of second item:")
    if item_2 in menu:
        order_total+=menu[item_2]
    
        print(f"your item {item_2} has been added to your order ")
    else:
       print(f"order item {item_2} is not available yet")
print(f"the total amount you have to pay is {order_total}")



