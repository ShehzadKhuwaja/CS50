import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"
    if match := re.search(regex, ip):
        return True
    else:
        return False

    
if __name__ == "__main__":
    main()
