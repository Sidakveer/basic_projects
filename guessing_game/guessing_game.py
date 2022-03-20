import random
import re


answer = random.randint(1, 101)

print("Welcome to the guessing game!")
print("I am thinking of a number between 1 and 100")

difficulty = input("Choose difficulty. Type easy or hard").casefold


def check(n):
    if n == answer:
        return f"You got it. The answer is {answer}"
    elif n < answer:
        return "Too low."
    else:
        return "Too high."


if difficulty == "easy":
    attempts = 10

    guess = int(input("Please enter a number: "))
    for x in range(attempts):
        print(f"You have {attempts} attempts remaining")
        if guess == answer:
            print(f"You got it. The answer is {answer}")
            break
        elif guess < answer:
            print("Too low.")
        else:
            print("Too high.")
    print(f"Sorry you lost. The answer was {answer}")



else: 
    attempts = 5