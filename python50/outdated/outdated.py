MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def date_formate(s):
    if s[0].isalpha():
        try:
            month_date, year = s.split(",")
            month, date = month_date.split(" ")
            if month not in MONTH or not 1 <= int(date) <= 31:
                return False
        except ValueError:
            return False
    else:
        s = s.split("/")
        try:
            if not 1 <= int(s[0]) <= 12 or not 1 <= int(s[1]) <= 31:
                return False
        except ValueError:
            return False

    return True

def iso_8601(date):
    if date[0].isalpha():
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        return f"{int(year)}-{int(month_to_number(month)):02}-{int(day):02}"
    else:
        month, day, year = date.split("/")
        return f"{int(year)}-{int(month):02}-{int(day):02}"

def month_to_number(month):
    for i, m in enumerate(MONTH):
        if m == month:
            return i + 1
def main():
    date = input("Date: ")
    while not date_formate(date):
        date = input("Date: ")
    print(iso_8601(date))

main()
