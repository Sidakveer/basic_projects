import random
import re

def play_game():
    answer = random.randint(1, 101)

    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1 and 100")

    difficulty = input("Choose difficulty. Type easy or hard")

    guess_correct = False
    if difficulty == "easy".casefold():
        attempts = 10

        for x in range(attempts):
            print(f"You have {10 - x} attempts remaining")
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

        for x in range(attempts):
            print(f"You have {5 - x} attempts remaining")
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


while True:
    play = input("Would you like to play the guessing game y/n ? ")
    if play == "y":
        play_game()
    else:
        break