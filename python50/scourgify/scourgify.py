import sys
import csv


if len(sys.argv[1:]) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv[1:]) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

data = []
try:
    with open(sys.argv[1]) as f:
       reader = csv.DictReader(f)
       for row in reader:
           data.append(row) 
except FileNotFoundError:
    print("Could not read invalid_file.csv")
    sys.exit(1)

newdata = []
for row in data:
    last, first = row["name"].split(", ")
    newdata.append({"first": first, "last": last, "house": row["house"]})

with open(sys.argv[2], "w") as f:
    writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in newdata:
        writer.writerow(row)
    
