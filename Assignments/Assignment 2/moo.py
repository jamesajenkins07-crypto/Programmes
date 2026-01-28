#!/bin/python3

'''
FULL NAME: James Jenkins
STUDENT NUMBER: 251491498
UWO USERNAME: jjenki48
CREATION DATE: 2026-01-28
DESCRIPTION: Interactive cows & bulls game with use of string manipulation and randint.
'''


from random import randint

# Generate 5 digit number ensuring each are unique

answer = ''

while len(answer) < 5:
    addition = str(randint(1, 9))
    if addition not in answer:
        answer += addition

# Set initial variables
guess_count = 6
progress = "-" * 5

while guess_count > 0:

    # Set variables for each turn
    skip = False
    bulls = ''
    cows = ''
    guess = ''

    guess = input(f"Guess a five-digit number ({guess_count} guesses remaining): ")

    # Ensure clean input

    if not guess.isdecimal() or '0' in guess:
        print("Please only include the digits 1 through 9 in your guess.")
        print("This will not count against your number of guesses.")
        continue

    if len(guess) != 5:
        print("Please enter a five-digit number.")
        print("This will not count against your number of guesses.")
        continue

    for character in guess:
        if guess.count(character) > 1:
            skip = True

    # If multiple characters in guess go back to start
    if skip:
        print("Digits can only appear once in your guess.")
        print("This will not count against your number of guesses.")
        continue

    # Check if guess is correct
    if guess == answer:
        print(f"Congratulations! You solved the puzzle in {6-guess_count+1} guess(es)!")
        print(f"The answer was {answer}")
        break

    # Determine bulls or cows
    for character in guess:
        guess_index = guess.index(character)
        if character in progress:
            continue
        if character in answer:
            answer_index = answer.index(character)
            if guess_index == answer_index:
                first_progress_half = progress[:guess_index]
                second_progress_half = progress[guess_index + 1:]
                progress = first_progress_half + character + second_progress_half
                bulls += character
            else:
                cows += character

    # Print output
    if bulls == '':
        print("You did not find any bulls.")
    else:
        print(f"You found {len(bulls)} bull(s): {bulls[0]}", end='')
        for bull in bulls[1:]:
            print(" and", bull, end='')
        print(".")
    if cows == '':
        print("You did not find any cows.")
    else:
        print(f"You found {len(cows)} cow(s): {cows[0]}", end='')
        for cow in cows[1:]:
            print(" and", cow, end='')
        print(".")
    print(progress)
    print()

    guess_count -= 1

# Ensure output if loss
if guess_count == 0:
    print("Sorry, but you did not solve the puzzle.")
    print(f"The answer was {answer}")
