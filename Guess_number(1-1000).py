import random

guess = int (input ("Guess my number:"))

secret = random.randint(1,1000)

i = 4

while guess != secret and i:
    if guess > 1000 or guess < 1:
        print("The number is between 1 and 1000!")
        i = i - 1
    elif guess < secret:
        print("Smaller!")
        i = i - 1
    else:
        print("Bigger!")
        i = i - 1
        print("Remaining chances:", i)
    guess = int (input ("Guess my number:"))

else:
    if (i > 0):
        print("Bingo!\nUsed chances:", i)
    else:
        print("You used all chances!\nGame over!")