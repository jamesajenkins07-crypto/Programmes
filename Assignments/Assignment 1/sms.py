#!/bin/python3

'''
FULL NAME: James Jenkins
STUDENT NUMBER: 251491498
UWO USERNAME: jjenki48
CREATION DATE: 2026-01-15
DESCRIPTION: SMS moderator billing calculator. Reads message, cost per
segment, and a banned word, then produces cleaned preview with
billing info.
'''


from math import ceil

# Take text input

message = input("Enter the SMS message text: ")
rate = float(input("Enter the SMS cost per segment: $"))
censor = input("Enter the word to censor: ")

# Clean text

message = message.strip()
message = message.lower()

censor = censor.lower()
message = message.replace(censor, "***")

# Calculate cost

message_segments = len(message) / 160
message_segments = ceil(message_segments)

cost = message_segments * rate
cost = round(cost, 2)

# Output

print(("=" * 30))
print(message)
print(("=" * 30))
print("Characters:", len(message))
print("Segments:", message_segments)
print("Cost: $" + str(cost))
