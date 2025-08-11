# Define Main function
def main():
        
    # Ask user to enter emoticon
    emotIcon = input("Enter emoticon: ")
    
    # Convert emoticon to emoji using Convert()
    emoji = convert(emotIcon)

    # Print emjoi
    print(emoji)


# Define Convert function
def convert(emotIcon):

    # Convert emoticon to emoji
    emoji1 = emotIcon.replace(":)", "🙂")
    emoji2 = emoji1.replace(":(", "🙁")

    # Return emoji
    return emoji2

main()