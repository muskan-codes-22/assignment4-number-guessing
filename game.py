import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 50)

while True:
    guess = int(input("Enter your guess (1-50): "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it!")
        break
