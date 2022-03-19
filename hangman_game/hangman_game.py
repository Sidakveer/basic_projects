import random
from asci_art import stages, logo
from word_list import word_list

chosen_word = random.choice(word_list).casefold()
lives = 6

print(chosen_word)

print(logo)
n = len(chosen_word)
blank_list = n*["_"]
print(blank_list)

while lives != 0 and "".join(blank_list) != chosen_word:
    choice = input("Please enter your guess: ").casefold()
    if choice in blank_list:
        print("You have already guessed this letter try another one!")

    elif choice in chosen_word:
        for index, letter in enumerate(chosen_word):
            if choice == letter:
                blank_list[index] = choice

        print(blank_list)
        print(stages[lives])

    else:
        lives -= 1
        print(blank_list)
        print(stages[lives])


if lives == 0:
    print("YOU LOST!")
    print(f"The correct word was {chosen_word}")
else:
    print("YOU GUESSED IT!")
    print(blank_list)