answer = 5

print("Please guess number between 1 and 10")
guess = int(input())

if guess < answer :
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else :
        print("Sorry you have not guessed it correctly")
elif guess > answer :
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else :
        print("Sorry you have not guessed it correctly")
else :
    print("You are right")