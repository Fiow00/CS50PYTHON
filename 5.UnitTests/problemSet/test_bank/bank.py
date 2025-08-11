def main():
    # Prompt a Greeting from user
    great = input("Greeting: ").strip().lower()
    money = value(great)
    print(f"${money}")

def value(greeting):
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        money = 0
    elif greeting.startswith("h") or greeting.startswith("H"):
        money = 20
    else:
        money = 100

    return money

if __name__ == "__main__":
    main()
