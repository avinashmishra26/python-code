import random

highest = 10
answer = random.randint(1, highest)

print("please guess number between 1 and {}".format(highest))

guess = -1

while guess != answer :
    guess = int(input())
    if( guess == answer):
        print("you got it now")
    elif guess > answer:
        print("your guess is higher")
    else :
        print("your guess is lower")


