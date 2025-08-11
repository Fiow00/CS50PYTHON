import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    print(countNumbers())

def countNumbers():
    try:
        number = 0
        with open(sys.argv[1], "r") as file:
            if sys.argv[1].endswith(".py"):
                lines = file.readlines()
                for line in lines:
                    if line.rstrip().startswith("#") or line.isspace():
                        number = number
                    else:
                        number = number + 1
            else:
                sys.exit("Not a python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

    return number

if __name__ == "__main__":
    main()