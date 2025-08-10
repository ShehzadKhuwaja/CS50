import csv
import tabulate
import sys

if len(sys.argv[1:]) == 0:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv[1:]) > 1:
    print("Too many command-line arguments")
    sys.exit(1)
elif sys.argv[1][-4:] != ".csv":
    print("Not a CSV file")
    sys.exit(1) 

menu = []
try:
    with open(sys.argv[1]) as f:
        reader = csv.reader(f)
        heading = next(reader)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

print(tabulate.tabulate(menu, headers=heading, tablefmt="grid"))