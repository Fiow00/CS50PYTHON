def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove $
    strip = d.strip("$")

    # Convert to float
    dollars = float(strip)

    # Return dollars
    return dollars


def percent_to_float(p):
    # Remove %
    strip = p.strip("%")

    # Convert to percent
    percent = float(strip)
    
    # Convert percent to tip
    tip = percent / 100

    return tip

main()