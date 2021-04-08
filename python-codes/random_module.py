import random

def get_integer(prompt):
    temp = input(prompt)
    if temp.isnumeric():
        return int(temp)
    print("{} is not valid".format(temp))

highest = 1000
answer = random.randint(1,highest)
guess = 0
guess_count = 1
print("please enter a number between 1 and {}: ".format(highest))

while True:
    guess = get_integer(": ")
    if guess == 0 :
        break
    elif guess == answer:
        print("well done you guessed in {} guesses".format(guess_count))
    else:
        if guess>answer:
            print("Go lower")
        else:
            print("Go higher")

    guess_count += 1                    



