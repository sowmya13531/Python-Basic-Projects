#Shopping cart program

fooditems = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food} item: $"))
        fooditems.append(food)
        prices.append(price)

print("-----Your CART-----")

for food in fooditems:
    print(food)
    #end=" " for side by side

    for price in prices:
        total += price
        print(f"Your total price is : ${total} ")