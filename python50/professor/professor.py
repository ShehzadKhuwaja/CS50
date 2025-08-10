from random import randint

LEVELS = [1, 2, 3]
TRIES = 3
TOTAL_QUESTIONS = 10

def main():
    level = get_level()
    while True:
        try:
            num_one = generate_integer(level)
            num_two = generate_integer(level)
            break
        except ValueError:
            level = get_level()
    
    score = 0 
    for _ in range(TOTAL_QUESTIONS):
        invalid = False
        try:
            answer = int(input(f"{num_one} + {num_two} = "))
        except ValueError:
            invalid = True
        correct_answer = False 
        for i in range(TRIES):
            if not invalid and answer == num_one + num_two:
                correct_answer = True
                score += 1
                break
            else:
                print("EEE")
                if i + 1 != TRIES:
                    try:
                        answer = int(input(f"{num_one} + {num_two} = "))
                    except ValueError:
                        invalid = True
                    else:
                        invalid = False
        if not correct_answer:
            print(f"{num_one} + {num_two} = {num_one + num_two}")
        num_one = generate_integer(level)
        num_two = generate_integer(level)

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in LEVELS:
                return level


def generate_integer(level):
    if level not in LEVELS:
        raise ValueError
    elif level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)



if __name__ == "__main__":
    main()
