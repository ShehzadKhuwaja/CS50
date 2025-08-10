from datetime import date
import sys
import inflect

def main():
    birthdate = input("Date of birth: ")
    try:
        print(convert(birthdate))
    except ValueError:
        sys.exit(1)

def convert(birthday):
    try:
        year, month, day = birthday.split("-")
        t1 = date(int(year), int(month), int(day))
    except ValueError:
        raise ValueError

    t2 = date.today() - t1
    minutes = round(t2.total_seconds() / 60)
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()