items = {}
while True:
    try:
        item = input()
        items[item] += 1
    except EOFError:
        break
    except KeyError:
        items[item] = 1

for item in sorted(items):
    print(items[item], item.upper())