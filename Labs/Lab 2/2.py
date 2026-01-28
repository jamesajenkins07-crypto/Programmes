#!/bin/python3 

IDEAL_CREDIT_SCORE = 720
userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the house: "))

if housePrice < 0: # Didn't account for negative house price
    print("Invalid house price")
    quit()

if userScore >= IDEAL_CREDIT_SCORE: # Incorrect order =>
    downPayment = 0.1 * housePrice
elif userScore < IDEAL_CREDIT_SCORE and userScore > 600: # Str variable error, should be int, alongside else if should be elif
    downPayment = 0.2 * housePrice
else:
    downPayment = 0.3 * housePrice
print("Your down payment is: ${}".format(downPayment))
