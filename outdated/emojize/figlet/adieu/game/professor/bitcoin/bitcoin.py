import requests
import sys

# Getting a JSON object
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit(1)
else:
    bitcoin_dict = response.json()
    # Current price of Bitcoin as a float
    bitcoin_price = bitcoin_dict["bpi"]["USD"]["rate_float"]


# User must specify one command-line argument:
# A floating point number that represents the number of Bitcoins.
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else: # The script name (sys.argv[0]) and one argument.
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        # Outputs the current cost of n Bitcoins in USD.
        print(f"${n * bitcoin_price:,.4f}")
        # Four decimal places. Comma as a thousands separator.