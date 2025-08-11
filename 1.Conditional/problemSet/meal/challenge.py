def main():

    # Prompt the user for the time.
    time = input("What is the time? ")

    # Convert time into hours
    hours = convert(time)

    # use cases
    if 7 <= hours <= 8:
        print("Breakfast!")
    elif 0 <= hours <= 1:
        print("Lunchtime!")
    elif 6 <= hours <= 7:
        print("Dinnertime!")
    else:
        print("", end="")


def convert(time):

    # Split time into 2 veriables
    hours, minutes = time.split(":")

    # Calculate total hours
    hours = int(hours)
    minutes = int(minutes) / 60
    total = hours + minutes

    if total > 12:
        total = total / 12
        return total
    else:
        return total

if __name__ == "__main__":
    main()
