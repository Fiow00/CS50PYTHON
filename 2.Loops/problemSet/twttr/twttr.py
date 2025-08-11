# prompt the user for a string
string = input("Input: ")

# pring output message
print("Output: ", end="")

# check for the removed letters
for character in string:
    match character:
        case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
            print("", end="")
        case _:
            print(character, end="")
