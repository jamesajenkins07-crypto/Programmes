#!/bin/python3
# booking.py

"""
Lucy Li
251498022
lli2249@uwo.ca
Created: March 16, 2026
File description: This file contains the room booking helper functions used to
load room and booking data, search and validate bookings, and save bookings.booking.py
Contains all functions for the room booking assignment.
There must be no executable code outside the function definitions in this file.
"""

# Clean a room number by converting it to uppercase and removing all non-alphanumeric characters.
# Parameters:
#   room_number: A string that may contain spaces, punctuation, or mixed case.
# Returns:
#   A cleaned room number string.


def clean_room_number(room_number: str):
    room_number = room_number.strip().upper()
    cleaned_number = ""

    for character in room_number:
        if character.isalnum():
            cleaned_number += character

    return cleaned_number

# Load room data from a CSV file and store it in a nested dictionary keyed by cleaned room number.
# Parameters:
#   file_name: The name of the CSV file to read.
# Returns:
#   A dictionary of room information keyed by cleaned room number.


def load_rooms(file_name: str):
    loaded_rooms = {}

    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        room = line.strip().split(",")
        room_number = clean_room_number(room[0])

        loaded_rooms[room_number] = {
            "building": room[1],
            "capacity": int(room[2]),
            "features": room[3].strip().split("|"),
        }

    return loaded_rooms

# Load booking data from a TSV file and store it as a list of booking dictionaries.
# Parameters:
#   file_name: The name of the TSV file to read.
# Returns:
#   A list of booking dictionaries with cleaned room numbers.


def load_bookings(file_name: str):
    loaded_bookings = []

    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        booking = line.rstrip("\n").split("\t")

        loaded_bookings.append(
            {
                "room_number": clean_room_number(booking[0]),
                "date": booking[1],
                "hour": int(booking[2]),
                "num_attendees": int(booking[3]),
                "purpose": booking[4],
            }
        )

    return loaded_bookings

# Print the information for one room in the required readable format.
# Parameters:
#   room_dict: The dictionary of rooms.
#   room_number: The cleaned room number to display.
# Returns:
#   Nothing.


def print_room_info(room_dict: dict, room_number: str):
    info = room_dict[room_number]

    print("Room:", room_number)
    print("Building:", info["building"])
    print("Capacity:", info["capacity"])
    print("Features:")

    for feature in info["features"]:
        print(feature)

# Find all rooms that contain a given feature tag.
# Parameters:
#   room_dict: The dictionary of rooms.
#   feature_tag: The feature tag to search for.
# Returns:
#   A list of cleaned room numbers that have the feature.


def find_rooms_by_feature(room_dict: dict, feature_tag: str):
    room_number_list = []

    for room in room_dict:
        if feature_tag in room_dict[room]["features"]:
            room_number_list.append(room)

    return room_number_list

# Find all rooms whose capacity is at least the given minimum.
# Parameters:
#   room_dict: The dictionary of rooms.
#   min_capacity: The minimum room capacity.
# Returns:
#   A list of cleaned room numbers that meet or exceed the capacity.


def find_rooms_by_capacity(room_dict: dict, min_capacity: int):
    room_number_list = []

    for room in room_dict:
        if room_dict[room]["capacity"] >= min_capacity:
            room_number_list.append(room)

    return room_number_list

# Return bookings that match a room number and/or date filter.
# Parameters:
#   bookings_list: The list of booking dictionaries.
#   room_number: A cleaned room number to filter by, or an empty string.
#   date: A booking date in YYYY-MM-DD format to filter by, or an empty string.
# Returns:
#   A list of matching booking dictionaries.


def find_bookings(bookings_list, room_number="", date=""):
    if room_number == "" and date == "":
        return bookings_list[:]

    relevant_bookings = []

    for booking in bookings_list:
        room_match = room_number == "" or booking["room_number"] == room_number
        date_match = date == "" or booking["date"] == date

        if room_match and date_match:
            relevant_bookings.append(booking)

    return relevant_bookings

# Remove a booking matching the given room number, date, and hour from the list.
# Parameters:
#   bookings_list: The list of booking dictionaries to modify.
#   room_number: The cleaned room number to remove.
#   date: The booking date to remove.
#   hour: The booking hour to remove.
# Returns:
#   True if a booking was removed, otherwise False.


def remove_booking(bookings_list: list, room_number: str, date: str, hour: int):
    for index, booking in enumerate(bookings_list):
        if (
            booking["room_number"] == room_number
            and booking["date"] == date
            and booking["hour"] == hour
        ):
            del bookings_list[index]
            return True

    return False

# Add a booking dictionary to the bookings list.
# Parameters:
#   bookings_list: The list of booking dictionaries to modify.
#   booking: The booking dictionary to add.
# Returns:
#   Nothing.


def add_booking(bookings_list: list, booking: dict):
    bookings_list.append(booking)

# Validate a new booking by checking room existence, date format, duplicate booking, and capacity.
# Parameters:
#   room_dict: The dictionary of rooms.
#   bookings_list: The current list of booking dictionaries.
#   new_booking: The booking dictionary to validate.
# Returns:
#   True if the booking is valid, otherwise False.


def validate_booking(room_dict: dict, bookings_list: list, new_booking: dict):
    room_number = new_booking["room_number"]

    if room_number not in room_dict:
        print("Invalid room!")
        return False

    date = new_booking["date"]
    parts = date.split("-")
    if (
        len(parts) != 3
        or len(parts[0]) != 4
        or len(parts[1]) != 2
        or len(parts[2]) != 2
        or not parts[0].isdigit()
        or not parts[1].isdigit()
        or not parts[2].isdigit()
    ):
        print("Invalid date!")
        return False

    for booking in bookings_list:
        if (
            booking["room_number"] == room_number
            and booking["date"] == date
            and booking["hour"] == new_booking["hour"]
        ):
            print("Room already booked at this date and time!")
            return False

    if new_booking["num_attendees"] > room_dict[room_number]["capacity"]:
        print("Room does not have required capacity!")
        return False

    return True

# Find bookings whose capacity percentage is below the given threshold.
# Parameters:
#   room_dict: The dictionary of rooms.
#   bookings_list: The list of booking dictionaries.
#   percentage: The under-booked threshold as a float between 0 and 1.
# Returns:
#   A list of tuples containing room number, date, hour, and capacity percentage.


def under_booked(room_dict: dict, bookings_list: list, percentage: float):
    results = []

    for booking in bookings_list:
        capacity = room_dict[booking["room_number"]]["capacity"]
        current_percentage = booking["num_attendees"] / capacity

        if current_percentage < percentage:
            results.append(
                (
                    booking["room_number"],
                    booking["date"],
                    booking["hour"],
                    current_percentage,
                )
            )

    return results

# Save the bookings list to a TSV file in the required format.
# Parameters:
#   bookings_list: The list of booking dictionaries to write.
#   file_name: The name of the TSV file to create.
# Returns:
#   Nothing.


def save_bookings(bookings_list: list, file_name: str):

    with open(file_name, "w") as file:
        file.write("room_number\tdate\thour\tnum_attendees\tpurpose\n")
        for booking in bookings_list:
            file.write(
                f'{booking["room_number"]}\t{booking["date"]}\t{booking["hour"]}\t'
                f'{booking["num_attendees"]}\t{booking["purpose"]}\n'
            )
