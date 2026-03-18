#!/bin/python3

total = 0
number = None
maximum = 0
count = -1

while number != 0:
    number = input("Enter an integer (0 to stop): ")

    try:
        number = int(number)
        count += 1
        total += number
        
        if number > maximum:
            maximum = number
    
    except ValueError:
        print("Invalid input. Please enter a whole number.")

average = total / count

print("Sum of values:", total)
print("Largest value:", maximum)
print("Average value:", average)
