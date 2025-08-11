months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop
while True:
    try:
        # Prompt user for date
        date = input("Date: ").title()

        # case /
        if '/' in date:
            month, day, year = date.split('/')
            month, day, year = int(month), int(day), int(year)
            if month > 12 or day > 31:
                continue
            else:
                break

        # case ,
        elif ',' in date:
            date = date.replace(',', '')
            month, day, year = date.split(' ')
            if month in months:
                month = months.index(month) + 1
                month, day, year = int(month), int(day), int(year)
                if month > 12 or day > 31:
                    continue
                else:
                    break

    # The master row
    except ValueError:
        pass

# Formated date
print(f"{year}-{month:02}-{day:02}")
