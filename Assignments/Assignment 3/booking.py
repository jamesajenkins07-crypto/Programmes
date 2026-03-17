"""
James Jenkins
251491498
jjenki48@uwo.ca
Created: March 16, 2026
File description: This file contains the room booking helper functions used to
load room and booking data, search and validate bookings, and save bookings.booking.py."""

# This function cleans a room number by converting it to uppercase and removing all non-alphanumeric characters.
# Parameters:
#   room_number: A string that may contain spaces, punctuation, or mixed case.


def clean_room_number(room_number):
    room_number = room_number.strip().upper()
    cleaned_number = ''

    for character in room_number:
        if character.isalnum():
            cleaned_number += character

    return cleaned_number

# This function loads room data from a CSV file and stores it in a nested dictionary keyed by cleaned room number.
# Parameters:
#   file_name: The name of the CSV file to read.
# Returns:
#   A dictionary containing the loaded room data.


def load_rooms(file_name):
    file = open(file_name)
    file.readline()
    loaded_rooms = {}

    for room in file:
        room = room.split(",")
        temp_rooms = {}
        number = clean_room_number(room[0])
        temp_rooms['building'] = str(room[1])
        temp_rooms['capacity'] = int(room[2])
        temp_rooms['features'] = room[3].strip().split("|")
        loaded_rooms[number] = temp_rooms

    file.close()

    return loaded_rooms

# This function loads booking data from a TSV file and stores it as a list of booking dictionaries.
# Parameters:
#   file_name: The name of the TSV file to read.
# Returns:
#   A list of dictionaries containing the loaded booking data.


def load_bookings(file_name):
    file = open(file_name)
    file.readline()
    loaded_bookings = []

    for booking in file:
        booking = booking.split("\t")
        booking[-1] = booking[-1].strip()
        temp_bookings = {}
        temp_bookings['room_number'] = clean_room_number(booking[0])
        temp_bookings['date'] = str(booking[1])
        temp_bookings['hour'] = int(booking[2])
        temp_bookings['num_attendees'] = int(booking[3])
        temp_bookings['purpose'] = str(booking[4])

        loaded_bookings.append(temp_bookings)

    return loaded_bookings

# This function prints the information of a room given its cleaned room number.
# Parameters:   room_dict: A dictionary containing room information keyed by cleaned room number.
#               room_number: The cleaned room number to look up in the dictionary.


def print_room_info(room_dict, room_number):
    info = room_dict[room_number]

    print("Room:", room_number)
    print("Building:", info['building'])
    print("Capacity:", info['capacity'])
    print("Features:")

    for feature in info['features']:
        print(feature)

# This function finds rooms that have a specified feature.
# Parameters:  room_dict: A dictionary containing room information keyed by cleaned room number.
#              feature_tag: The feature to search for in the rooms.
# Returns: A list of cleaned room numbers that contain the specified feature.


def find_rooms_by_feature(room_dict, feature_tag):
    room_number_list = []

    for room in room_dict:
        if feature_tag in room_dict[room]['features']:
            room_number_list.append(room)

    return room_number_list

# This function finds rooms that have a capacity greater than or equal to a specified minimum.
# Parameters:  room_dict: A dictionary containing room information keyed by cleaned room number.
#              min_capacity: The minimum capacity to search for.
# Returns: A list of cleaned room numbers that meet the capacity requirement.


def find_rooms_by_capacity(room_dict, min_capacity):
    room_number_list = []

    for room in room_dict:
        if min_capacity <= room_dict[room]['capacity']:
            room_number_list.append(room)

    return room_number_list

# This function finds bookings that match a specified room number and/or date.
# Parameters:  bookings_list: A list of dictionaries containing booking information.
#              room_number: The cleaned room number to search for (optional).
#              date: The date to search for (optional).
# Returns: A list of booking dictionaries that match the search criteria.


def find_bookings(bookings_list, room_number="", date=""):
    relevant_bookings = []
    if room_number == "" and date == "":
        return bookings_list

    for room in bookings_list:
        number = room['room_number']
        time = room['date']
        if room_number and not date:
            if number == room_number:
                relevant_bookings.append(room)
        if not room_number and date:
            if date == time:
                relevant_bookings.append(room)
        else:
            if date == time and number == room_number:
                relevant_bookings.append(room)

    return relevant_bookings

# This function removes a booking that matches a specified room number, date, and hour.
# Parameters:  bookings_list: A list of dictionaries containing booking information.
#              room_number: The cleaned room number of the booking to remove.
#              date: The date of the booking to remove.
#              hour: The hour of the booking to remove.
# Returns: True if a booking was removed, False if no matching booking was found.


def remove_booking(bookings_list, room_number, date, hour):
    located_booking = find_bookings(bookings_list, room_number=room_number, date=date)

    for booking in located_booking:
        if booking['hour'] == hour:
            bookings_list.remove(booking)
            return True

    return False

# This function adds a new booking to the list of bookings.
# Parameters:  bookings_list: A list of dictionaries containing booking information.


def add_booking(bookings_list, booking):
    bookings_list.append(booking)

# This function validates a new booking against the room data and existing bookings.
# Parameters:  room_dict: A dictionary containing room information keyed by cleaned room number.
#              bookings_list: A list of dictionaries containing existing booking information.
#              new_booking: A dictionary containing the new booking information to validate.
# Returns: True if the new booking is valid, False if it is invalid.


def validate_booking(room_dict, bookings_list, new_booking):
    if new_booking['room_number'] in room_dict:
        date = new_booking['date']
        if len(date) == 10:
            year = date[0:4]
            month = date[5:7]
            day = date[8:]
            if year.isdigit() and month.isdigit() and day.isdigit() and date[4] == "-" and date[7] == "-":
                if int(year) > 0 and 0 <= int(month) <= 12 and 0 <= int(day) <= 31:
                    double_booked = False

                    for prev_bookings in bookings_list:
                        new_date = new_booking['date']
                        prev_date = prev_bookings['date']
                        new_hour = new_booking['hour']
                        prev_hour = prev_bookings['hour']

                        if new_date == prev_date and new_hour == prev_hour:
                            double_booked = True

                    if not double_booked:
                        if not new_booking['num_attendees'] > room_dict[new_booking['room_number']]['capacity']:
                            return True

                        else:
                            print("Room does not have required capacity!")
                            return False
                    else:
                        print("Room already booked at this date and time!")
                        return False
                else:
                    print("Invalid date!")
                    return False
            else:
                print("Invalid date!")
                return False
        else:
            print("Invalid date!")
            return False
    else:
        print("Invalid room!")
        return False

# This function finds bookings whose capacity percentage is below the given threshold.
# Parameters:  room_dict: A dictionary containing room information keyed by cleaned room number.
#              bookings_list: A list of dictionaries containing booking information.
#              percentage: The under-booked threshold as a float between 0 and 1.
# Returns: A list of tuples containing room number, date, hour, and capacity percentage.


def under_booked(room_dict, bookings_list, percentage):
    under_bookings = []

    for booking in bookings_list:
        booked_cap = booking['num_attendees']
        room_cap = room_dict[booking['room_number']]['capacity']
        capacity_percent = booked_cap / room_cap

        if capacity_percent < percentage:
            number = booking['room_number']
            time_date = booking['date']
            time_hour = booking['hour']
            under_bookings.append((number, time_date, time_hour, capacity_percent))

    return under_bookings

# This function saves the current list of bookings to a TSV file.
# Parameters:  bookings_list: A list of dictionaries containing booking information.
#              file_name: The name of the TSV file to write to.


def save_bookings(bookings_list, file_name):
    file = open(file_name, "w")
    header = ["room_number", "date", "hour", "num_attendees", "purpose"]
    file.write("\t".join(header) + "\n")
    for booking in bookings_list:
        booking_number = booking["room_number"]
        booking_date = booking["date"]
        booking_hour = str(booking["hour"])
        booking_attendees = str(booking["num_attendees"])
        booking_purpose = booking["purpose"]
        line = [booking_number, booking_date, booking_hour, booking_attendees, booking_purpose]
        file.write("\t".join(line) + "\n")
    file.close()

# This function displays the main menu and prompts the user for a selection.
# Parameters: None.


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
            break
        else:
            print("Invalid input! Try again.")

    return int(selection)
