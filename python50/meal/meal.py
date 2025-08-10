def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, min = time.split(":")
    min = int(min) / 60
    return int(hour) + min


if __name__ == "__main__":
    main()
