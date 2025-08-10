import sys
import requests

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)

try:
    coins = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = r.json()
except requests.RequestException:
    pass

rate = r["bpi"]["USD"]["rate"]
f_rate = ""
for c in rate:
    if c != ",":
        f_rate += c
print(f"${coins*float(f_rate):,.4f}")
