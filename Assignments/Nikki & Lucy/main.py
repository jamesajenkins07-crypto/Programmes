#!/bin/python3
# main.py

"""
Lucy Li
251498022
lli2249@uwo.ca
Created: March 16, 2026
File description: This file contains the room booking helper functions used to
load room and booking data, search and validate bookings, and save bookings.
"""

from booking import *


def main_menu():
    print("\nSelect an option:")
    print("1) Display room information.")
    print("2) Search for room by feature.")
    print("3) Search for room by capacity.")
    print("4) Search for booking.")
    print("5) Make booking.")
    print("6) Remove booking.")
    print("7) Find under booked rooms.")
    print("8) Save bookings.")
    print("9) Exit.")

    while True:
        selection = input("\nInput selection (1-9): ")
        if selection.isdigit() and 1 <= int(selection) <= 9:
            return int(selection)
        print("Invalid input! Try again.")


rooms = load_rooms("rooms.csv")
bookings = load_bookings("bookings.tsv")

while True:
    selection = main_menu()

    if selection == 1:
        room_input = input("Input room number: ")
        cleaned = clean_room_number(room_input)
        if cleaned not in rooms:
            print("Invalid room number!")
        else:
            print_room_info(rooms, cleaned)

    elif selection == 2:
        feature = input("Input feature to search for: ")
        matching = find_rooms_by_feature(rooms, feature)
        if not matching:
            print("No rooms found!")
        else:
            print("Matching rooms:", ", ".join(matching))

    elif selection == 3:
        min_cap = int(input("Input minimum capacity to search for: "))
        matching = find_rooms_by_capacity(rooms, min_cap)
        if not matching:
            print("No rooms found!")
        else:
            print("Matching rooms:", ", ".join(matching))

    elif selection == 4:
        room_input = input("Input room number (or leave empty for all rooms): ")
        date_input = input("Input date (or leave empty for all dates): ")
        cleaned = clean_room_number(room_input)

        results = find_bookings(bookings, cleaned, date_input)
        if not results:
            print("No bookings found!")
        else:
            for booking in results:
                print("Room:", booking["room_number"])
                print("Date:", booking["date"])
                print("Hour:", booking["hour"])
                print("Attendees:", booking["num_attendees"])
                print("Purpose:", booking["purpose"])
                print("------------------------------")

    elif selection == 5:
        room_input = input("Input room number to book: ")
        date_input = input("Input date to book: ")
        hour_input = int(input("Input hour to book: "))
        attendees_input = int(input("Input number of attendees: "))
        purpose_input = input("Input purpose of booking: ")

        new_booking = {
            "room_number": clean_room_number(room_input),
            "date": date_input,
            "hour": hour_input,
            "num_attendees": attendees_input,
            "purpose": purpose_input,
        }

        if validate_booking(rooms, bookings, new_booking):
            add_booking(bookings, new_booking)
            print("Booked.")
        else:
            print("Booking not made!")

    elif selection == 6:
        room_input = input("Input room number: ")
        date_input = input("Input date: ")
        hour_input = int(input("Input hour: "))

        cleaned = clean_room_number(room_input)

        if remove_booking(bookings, cleaned, date_input, hour_input):
            print("Booking removed.")
        else:
            print("Booking not found!")

    elif selection == 7:
        under = under_booked(rooms, bookings, 0.2)
        print("Under booked rooms:")
        print("Room       Date          Hour   Percent Capacity")
        for room_number, date, hour, pct in under:
            print(f"{room_number:<10} {date:<12} {hour:<5} {pct * 100:.1f}%")

    elif selection == 8:
        file_name = input("Input file name to save bookings in: ")
        save_bookings(bookings, file_name)
        print("Saved!")

    elif selection == 9:
        break
