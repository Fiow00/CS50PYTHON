# Prompt camelCase from user
string = input("camelCase: ")

# Convert camelCase into snake_case
for character in string:
    if character.isupper():
        print("_" + character.lower(), end="")
    else:
        print(character, end="")

