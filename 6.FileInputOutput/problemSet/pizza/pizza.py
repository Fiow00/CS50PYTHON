import sys; from tabulate import tabulate; import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    table = []

    try:
        with open(sys.argv[1], "r", newline="") as file:
            if sys.argv[1].endswith(".csv"):
                reader = csv.DictReader(file)
                for line in reader:
                    table.append(line)
            else:
                sys.exit("Not a csv file")
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()