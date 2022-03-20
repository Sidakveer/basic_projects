import random
import re


answer = random.randint(1, 101)

print("Welcome to the guessing game!")
print("I am thinking of a number between 1 and 100")

difficulty = input("Choose difficulty. Type easy or hard").casefold

guess_correct = False
if difficulty == "easy":
    attempts = 10

    for x in range(attempts):
        print(f"You have {attempts} attempts remaining")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it. The answer is {answer}")
            guess_correct = True
            break
        elif guess < answer:
            print("Too low.")
        else:
            print("Too high.")
            
    if not guess_correct:
        print(f"Sorry you lost. The answer was {answer}")



else:
    attempts = 5
