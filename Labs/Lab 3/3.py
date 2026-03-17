#!/bin/python3

password = input("Enter a password: ")

upper = False
number = False
symbol = False
length = False

if len(password) > 8:
    length = True

for character in password:
    if character.isupper():
        upper = True
    if character.isdigit():
        number = True
    if character in "!@#$%^&*()":
        symbol = True

print("Upper", upper)
print("number", number)
print("symbol", symbol)
print("length", length)

if upper and number and length and symbol:
    print("Password accepted!")
else:
    print("Invalid password!")

