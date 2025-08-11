# Empty dictionary
items = {

}

# Loop
while True:

    # Prompt user for an item
    try:
        item = input().upper()

        # Use case
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    except EOFError:
        print()
        break
    except KeyError:
        pass

# Print items
for item in sorted(items):
    print(items[item], item)
    