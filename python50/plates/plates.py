import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha() or len(s) > 6 or len(s) < 2 or interwine(s) or first_digit_zero(s):
        return False
    if has_punctuation(s) or s.find(" ") != -1:
        return False
    
    return True

def interwine(s):
    digit_discovered = False
    for c in s:
        if c.isdigit() and not digit_discovered:
            digit_discovered = True
        elif c.isalpha() and digit_discovered:
            return True
    return False

def first_digit_zero(s):
    for c in s:
        if c.isdigit() and c == "0":
            return True
        if c.isdigit() and c != "0":
            return False
    return False

def has_punctuation(s):
    for c in s:
        if c in string.punctuation:
            return True
    return False

main()
