#!/bin/python3 

def calc (div):
    try:
        q = 12 / div
        print(q)
    except:
        print("Cannot divide by 0!")

def main ():
    div = input("Enter a divisor: ")
    try:
        div = int(div)
        calc(div)
        print("Finished")
    except ValueError:
        print("Cannot convert to an int!")

while True:
    main()
