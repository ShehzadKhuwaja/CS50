names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

print()
print("Adieu, adieu, to ", end="")
if len(names) == 1:
    print(f"{names[0]}")
elif len(names) == 2:
    print(f"{names[0]} and {names[1]}")
else:
    print(*names[:-1], sep=", ", end="")
    print(f", and {names[-1]}")