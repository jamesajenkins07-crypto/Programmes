#!/bin/python3

'''
FULL NAME: James Jenkins
STUDENT NUMBER: 251491498
UWO USERNAME: jjenki48
CREATION DATE: 2026-01-15
DESCRIPTION: Download time estimator. Reads a file size in MB and a download
speed in Mbps, converts units, computes total download time,
and prints result in H:MM:SS format.
'''

# Read inputs

file_size = float(input("Enter the file size (in MB): "))
download_speed = float(input("Enter the download speed (in Mbps): "))

# Convert units

file_size *= 8

# Estimate download time in seconds

total_seconds = round(file_size / download_speed)

# Break into hours, minutes, & seconds

hours = total_seconds // (60 * 60)
minutes = (total_seconds % (60 * 60)) // 60
seconds = ((total_seconds % (60 * 60)) % 60)

time = str(int(hours)) + ":" + str(int(minutes)) + ":" + str(int(seconds))

# Print output

print("Estimated download time:", time)
