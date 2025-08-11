# print that amoutDue = 50
amountDue = 50

# ask user for input as long as amountDue > 0
while amountDue > 0:

    print(f"Amount Due: {amountDue}")

    coin = int(input("Insert coin: "))

    if coin in [25, 10, 5]:
        amountDue = amountDue - coin

change_owed = abs(amountDue)
print("Change Owed:", change_owed)

