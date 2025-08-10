while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        while x > y:
            x, y = input("Fraction: ").split("/")
        percentage = round(x / y * 100)
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

