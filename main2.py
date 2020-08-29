import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

number = random.randrange(0,11)
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == number:
    print("Winner winner, chicken dinner!")
else:
    print("Whoops, not good enough.")
    print("The number was " + str(number))