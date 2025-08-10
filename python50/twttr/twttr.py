VOWELS = "aeiou"
txt = input("Input: ").strip()
print("Output: ", end="")
for c in txt:
    if c.lower() not in VOWELS:
        print(c, end="")
print()