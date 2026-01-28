#!/bin/python3

temperature = int(input("Enter the current temperature in degrees Celsius: "))
weather = input("Enter the current weather condition (sunny, rainy, snowy, windy): ")

if temperature > 25 and weather == "sunny":
    print("Wear light clothing, sunglasses, and a hat.")
elif 15 < temperature <= 25 and weather == "windy":
    print("Wear a light jacket and comfortable pants.")
elif 5 < temperature <= 15 and weather == "rainy": 
    print("Wear a raincoat and waterproof boots.")
elif temperature < 5 and weather == "snowy":
    "Wear a heavy coat, scarf, gloves, and warm boots."
else:
    print("Dress comfortably and check the forecast for details.")
