#!/bin/python3

def inches_to_cm(inches):
    return inches * 2.54

def feet_to_inches(feet):
    return feet * 12

def convert_height():
    print("Enter your height:")
    num_feet = int(input("Feet: "))
    num_inches = int(input("Inches: "))
    print("Your height in centimetres:", inches_to_cm(feet_to_inches(num_feet)) + inches_to_cm(num_inches), "cm")

convert_height()
