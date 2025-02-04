#concession stand program
menu = {"pizza": 3.00,
        "water": 4.56,
        "corn": 9.00,
        "frenchfries": 7.88,
        "kure": 6.88,
        "soda": 8.65,
        "tea": 6.12,
        "drink": 6.23}
cart = []
total = 0
print("-----------Menu----------")
for key,value in menu.items():
    print(f"{key}: ${value:.2f}")
print("------------------------------")
while True:
    food = input("Selet an item (q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------Your order-----------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")
print()
print(f"total is : ${total:.2f}")

