"""Biction"""

# Import required modules
import json
import requests
import sys

# Check Command-line arguments
while True:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        if sys.argv[1].isalpha():
            sys.exit("Command-line argument is not a number")
        else:
            break
    else:
        sys.exit()

# Get data from Api
try:
    response = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')
    date = response.json()

    # Get the price from json file and convert it to float
    price = date["bpi"]["USD"]["rate"].replace(",", "")
    price = float(price)

    # Conver command line 2 to float
    value = float(sys.argv[1])
    amount = price * value

    # Return price places with thousands seperator
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()