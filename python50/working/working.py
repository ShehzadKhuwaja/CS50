import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"^([1]?\d [AP]M) to ([1]?\d [AP]M)$|^([1]?\d:[0-5]\d [AP]M) to ([1]?\d:[0-5]\d [AP]M)$"
    if match := re.search(regex, s):
        start1, end1, start2, end2 = match.groups()
        if start1 is not None:
            return f"{unit_conversion(start1)} to {unit_conversion(end1)}"
        else:
            h1, m1 = hm_format(start2)
            h2, m2 = hm_format(end2)
            return f"{unit_conversion(h1, m1)} to {unit_conversion(h2, m2)}"
    else:
        raise ValueError


def hm_format(time):
    h, m = time[:-3].split(":")
    h = f"{h}{time[-3:]}"
    return (h, m)    

def unit_conversion(start, min="00"):
    if "AM" in start:
        if int(start[:-3]) != 12:
            s_time = f"{start[:-3]}:{min}" 
        else:
            s_time = f"00:{min}"
    else:
        if int(start[:-3]) != 12:
            s_time = f"{int(start[:-3]) + 12}:{min}"
        else:
            s_time = f"12:{min}"
    if len(s_time) != 5:
        return "0"+ s_time
    else: 
        return s_time

if __name__ == "__main__":
    main()
