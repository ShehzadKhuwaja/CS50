from random import randrange

def get_input(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            pass
        else:
            if num > 0:
                break
    return num

try:
    target = randrange(1, get_input("Level: "))
except ValueError:
    target = 1
guess = get_input("Guess: ")

while guess != target:
    print("Too small!") if guess < target else print("Too large!")
    guess = get_input("Guess: ")

print("Just right!")
