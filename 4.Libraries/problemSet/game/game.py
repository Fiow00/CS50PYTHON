"""Guessing game"""

# Import required Modules
import random

# Loop
while True:
    # Level
    try:
        # Prompt the user for level
        level = int(input("Level: "))
        # Check if level > or = to 0
        if level >= 0:
            # Guess >= 0
            try:
                # Prompt the user for Guess
                Guess = int(input("Guess: "))
                # Use cases
                if Guess >= 0:
                    number = random.randint(1, 100)
                    if Guess > number:
                        print("Too large!")

                    elif Guess < number:
                        print("Too small!")

                    else:
                        print("Just right!")
                        break

            # When user inputed string
            except ValueError:
                pass
    # When user inputed string
    except ValueError:
        pass
