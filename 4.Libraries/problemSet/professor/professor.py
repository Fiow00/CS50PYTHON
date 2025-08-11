"""Professor"""

# Import required modules
import random


# Main Function
def main():
    score = 0
    wrong_answer = 0
    level = get_level()

    # 10 Questions
    for _ in range(10):
        first_integer, second_integer = generate_integer(level)
        while True:
            try:
                answer = int(input(f"{first_integer} + {second_integer} = "))
                try:
                    if answer == first_integer + second_integer:
                        score = score + 1
                        break
                    elif answer != first_integer + second_integer:
                        if wrong_answer < 2:
                            print("EEE")
                            wrong_answer = wrong_answer + 1
                            continue
                        elif wrong_answer == 2:
                            print("EEE")
                            print(
                                f"{first_integer} + {second_integer} = {first_integer + second_integer}"
                            )
                            wrong_answer = 0
                            break
                except ValueError:
                    print("EEE")
            except ValueError:
                if wrong_answer < 2:
                    print("EEE")
                    wrong_answer = wrong_answer + 1
                elif wrong_answer == 2:
                    print("EEE")
                    print(
                        f"{first_integer} + {second_integer} = {first_integer + second_integer}"
                    )
    # print total Score.
    print(f"Score: {score}")


# Get level
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level < 1:
                continue
            else:
                break
        except ValueError:
            ...
    return level


# Generate numbers depends on each level
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


# ??? ill read about it later
if __name__ == "__main__":
    main()
