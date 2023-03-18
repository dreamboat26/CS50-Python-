import random
def main():
    answer_list = []
    level = get_level()
    # Randomly generates ten (10) math problems.
    problems = 10
    while problems != 0:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3
        while tries != 0:
    # Allows three tries in case of incorrect answer.
            answer = input(f"{x} + {y} = ")
            if int(answer) != x + y:
                print("EEE")
                tries -= 1
                if tries == 0:
                    print(f"{x} + {y} = {x+y}")
                    problems -= 1
            else:
                problems -= 1
                answer_list.append(answer)
                break # Breaks out of the while tries loop

    # Outputs the score, a number out of 10.
    if problems == 0:
        print(f"Score: {len(answer_list)}")

def get_level():
    # Prompts the user for a level and returns 1, 2 or 3.
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n in [1, 2, 3]:
                return n


def generate_integer(level):
    # Returns a randomly generated non-negative integer with level digits.
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()