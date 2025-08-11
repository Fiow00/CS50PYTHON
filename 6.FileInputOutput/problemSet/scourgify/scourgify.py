import csv; import sys;

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        names = []
        with open(sys.argv[1], 'r', newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                fname, lname = line['name'].split(", ")
                house = line['house']
                names.append({"fname": fname, "lname": lname, "house": house})

        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['fname','lname','house'])
            for name in names:
                writer.writerow(name)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()