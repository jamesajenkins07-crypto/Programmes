#!/bin/python3

'''
FULL NAME: James Jenkins
STUDENT NUMBER: 251491498
UWO USERNAME: jjenki48
CREATION DATE: 2026-01-15
DESCRIPTION: Weather index calculator. Reads temperature (C), humidity (0-1),
and wind speed (km/h) from the user and prints the Wind Chill Index (C) and
Humidex rounded to one decimal place.
'''

# Read inputs
temperature = int(input("Enter temperature (C): "))
humidity = float(input("Enter humidity (0 to 1): "))
wind_speed = int(input("Enter wind speed (km/h): "))

# Wind chill calculation using the Canadian wind chill formula

wind_chill = (13.12 + (0.6215 * temperature) -
              (11.37 * wind_speed ** 0.16) +
              (0.3965 * temperature * (wind_speed ** 0.16)))

# Humidex calculation

saturation_vapour = 6.11 * 10 ** ((7.5*temperature) / (237.3 + temperature))
actual_vapour = humidity * saturation_vapour
humidex = temperature + 0.5555 * (actual_vapour - 10)

# print calculations

print("")
print("Wind Chill Index:", round(wind_chill, 1), "C")
print("Humidex:", round(humidex, 1))
