import random
while True:
    try:
        level=int(input("Level: "))    #level is used for setting the range for random generation
        if level>0:
            break
    except:
        pass
random_number=random.randint(1,level)
while True:
    try:
        guess=int(input("Guess: "))
        if guess>0:
            if guess< random_number:
                print("Too small!")
            elif guess> random_number:
                print("Too Large!")
            else:
                print("Just Right!")
                break
    except:
        pass

