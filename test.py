#!/bin/python3

from random import choice

options = ["A", "B", "C", "D", "E"]
while True:
    num_questions = input("Number of questions: ")

    if num_questions.isdecimal():
        if int(num_questions) > 0:
            break
        else:
            print("Error: Inalid input, try again!")
            continue
    else:
        print("Error: Invalid input, try again!")
        continue

for question in range(1, (int(num_questions)+1)):
    print(f"{question}. {choice(options)}")
