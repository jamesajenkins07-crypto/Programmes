"""
James Jenkins
251491498
jjenki48@uwo.ca
Created: March 16, 2026
File description: This file contains the main program loop for the room booking assignment.
It loads room and booking data, displays a menu of options to the user,
and calls the appropriate functions based on user input.
The program continues until the user chooses to exit.
"""

from booking import *

rooms = load_rooms("rooms.csv")
bookings = load_bookings("bookings.tsv")

while True:
    selection = main_menu()

    if selection == 1:
        room_number = clean_room_number(input("Input room number: "))
        try:
            print_room_info(rooms, room_number)

        except KeyError:
            print("Invalid room number!")

    elif selection == 2:
        feature = input("Input feature to search for: ")
        found_feature_rooms = find_rooms_by_feature(rooms, feature)

        if found_feature_rooms == []:
            print("No rooms found!")
        else:
            print("Matching rooms:", ", ".join(found_feature_rooms))

    elif selection == 3:
        min_capacity = int(input("Input minimum capacity to search for: "))
        found_capacity_rooms = find_rooms_by_capacity(rooms, min_capacity)

        if found_capacity_rooms == []:
            print("No rooms found!")

        else:
            print("Matching rooms:", ", ".join(found_capacity_rooms))

    elif selection == 4:
        room_number = clean_room_number(input("Input room number (or leave empty for all rooms): "))
        date = input("Input date (or leave empty for all dates): ")

        found_bookings = find_bookings(bookings, room_number, date)

        if found_bookings == []:
            print("No bookings found!")

        else:
            for booking in found_bookings:
                print("Room:", booking["room_number"])
                print("Date:", booking["date"])
                print("Hour:", booking["hour"])
                print("Attendees:", booking["num_attendees"])
                print("Purpose:", booking["purpose"])
                print("------------------------------")

    elif selection == 5:
        new_booking = {}
        new_booking["room_number"] = clean_room_number(input("Input room number to book: "))
        new_booking["date"] = input("Input date to book: ")
        new_booking["hour"] = int(input("Input hour to book: "))
        new_booking["num_attendees"] = int(input("Input number of attendees: "))
        new_booking["purpose"] = input("Input purpose of booking: ")

        if validate_booking(rooms, bookings, new_booking):
            add_booking(bookings, new_booking)
            print("Booked.")

        else:
            print("Booking not made!")

    elif selection == 6:
        room_number = clean_room_number(input("Input room number: "))
        date = input("Input date: ")
        hour = int(input("Input hour: "))

        if remove_booking(bookings, room_number, date, hour):
            print("Booking removed.")
        else:
            print("Booking not found!")

    elif selection == 7:
        under_booked_rooms = under_booked(rooms, bookings, 0.9)

        print(f"{"Room":<10}{"Date":<12}{"Hour":<8}{"Percent Capacity":<20}")

        for room in under_booked_rooms:
            percent = room[3] * 100
            formatted_percent = f"{percent:.1f}%"
            print(f"{room[0]:<10}{room[1]:<12}{room[2]:<8}{formatted_percent:<20}")

    elif selection == 8:
        name = input("Input file name to save bookings in: ")
        save_bookings(bookings, name)
        print("Saved!")

    elif selection == 9:
        break
