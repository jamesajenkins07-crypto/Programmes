#!/bin/python3 

# Shop Programme
shopName = input("Please enter the shop name: ") 
ringQTY = int(input("Please enter ring QTY: ")) 
glassesQTY = int(input("Please enter glasses QTY: ")) 
print(f"Shop name is {shopName}") 
print(f"Ring QTY is {ringQTY}") 
print(f"Glasses QTY is {glassesQTY}") 
total = ringQTY+glassesQTY 
print(f"Inventory Total: {total}")  

# Fahrenheit to Celsius Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is {fahrenheit:.1f}.")
