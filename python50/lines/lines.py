import sys


if len(sys.argv[1:]) == 0:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv[1:]) > 1:
    print("Too many command-line arguments")
    sys.exit(1)
elif sys.argv[1][-3:] != ".py":
    print("Not a Python file") 
    sys.exit(1)

count = 0
try:
    with open(sys.argv[1]) as f:
        for line in f:
            if line.lstrip().startswith("#") or line.isspace():
                continue
            else: 
                count+= 1
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)


print(count)