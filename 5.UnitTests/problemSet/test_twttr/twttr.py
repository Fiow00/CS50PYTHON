# main
def main():
    word = shorten("What's your name?")
    print(word)

# Convert text
def shorten(word):
    new_word = ""
    for character in word:
        match character:
            case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
                new_word = new_word
            case _:
                new_word = new_word + character
    return new_word

if __name__ == "__main__":
    main()
