# Removes else

def main():
    x = get_int()
    print(f"")

def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an interger")

main()