# List of items with prices
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

totalPrice = 0

while True:
    # prompt item from user as long as user didn't finish
    try:
        item = input("Item: ").title()

        # Check if the order is in items list
        if item in items:

            # Get the price of the order
            price = items.get(item)

            # Count the Total price
            totalPrice = totalPrice + price

            # Print Total price
            print(f"Total: ${totalPrice:.2f}")
    # Once user input ctrl + d finished the program
    except EOFError:
        print()
        break
    except KeyError:
        pass

