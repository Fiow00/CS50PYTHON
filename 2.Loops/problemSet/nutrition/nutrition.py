# Fruits dictionary
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantalupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
}

# prompt user for a fruit
fruit = input("Item: ")

# check if fruit in fruits
while True:
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
        break
    else:
        break