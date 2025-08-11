def main():

    # Prompt the user for the time.
    time = input("What is the time? ")

    # Convert time into hours
    hours = convert(time)
    
    # use cases
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
    else:
        print("", end="")


def convert(time):

    # Split time into 2 veriables
    hours, minutes = time.split(":")

    # Convert hours and minutes into integers
    hours = int(hours)
    minutes = int(minutes) / 60

    return hours + minutes

if __name__ == "__main__":
    main()