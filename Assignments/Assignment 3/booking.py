"""
Starter template for booking.py.

You must replace this comment and fill in the details of each function
except for main_menu() which is provided for you. Make sure you remove
the pass keyword after you fill in the code for that function.

See Part 2 of the assignment document for details on the parameters,
return, and specification for each function.

There should be no code in this file outside of any of these function
definitions.
""" 

def clean_room_number(room_number : str):
    room_number = room_number.strip().upper()
    cleaned_number = ''

    for character in room_number:
        if character.isalnum():
            cleaned_number += character

    return cleaned_number

def load_rooms(file_name : str):
    from csv import reader
    file = list(reader(open(file_name)))
    loaded_rooms = {}
    
    for room in file[1:]:
        temp_rooms = {}
        number = clean_room_number(room[0])
        temp_rooms['building'] = str(room[1])
        temp_rooms['capacity'] = int(room[2])
        temp_rooms['features'] = room[3].strip().split("|")
        loaded_rooms[number] = temp_rooms

    return loaded_rooms

def load_bookings(file_name : str):
    from csv import reader
    file = list(reader(open(file_name), delimiter="\t"))
    loaded_bookings = []

    for booking in file[1:]:
        temp_bookings = {}
        temp_bookings['room number'] = clean_room_number(booking[0])
        temp_bookings['date'] = str(booking[1])
        temp_bookings['hour'] = int(booking[2])
        temp_bookings['num_atendees'] = int(booking[3])
        temp_bookings['purpose'] = str(booking[4])
        
        loaded_bookings.append(temp_bookings)

    return loaded_bookings

def print_room_info(room_dict : dict, room_number : str):
    info = room_dict[room_number]


    print("Room:", room_number)
    print("Building:", info['building'])
    print("Capacity:", info['capacity'])
    print("Features:")

    for feature in info['features']:
        print(feature)

def find_rooms_by_feature(room_dict : dict, feature_tag : str):
    room_number_list = []

    for room in room_dict:
        if feature_tag in room_dict[room]['features']:
            room_number_list.append(room)

    return room_number_list

def find_rooms_by_capacity(room_dict : dict, min_capacity : int):
    room_number_list = []

    for room in room_dict:
        if min_capacity <= room_dict[room]['capacity']:
            room_number_list.append(room)

    return room_number_list


def find_bookings(bookings_list : dict, room_number = "", date=""):
    relevant_bookings = []
    if room_number == "" and date == "":
        return bookings_list
    
    for room in bookings_list:
        number = room['room number']
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


def remove_booking(bookings_list : list, room_number : str, date : str, hour : int):
    located_booking = find_bookings(bookings_list, room_number = room_number, date = date)
    if located_booking == []:
        return False

    for booking in located_booking:
        if booking['hour'] == hour:
            booking_data.remove(booking)
            return True
        else:
            return False

def add_booking(bookings_list, booking):
    pass


def validate_booking(room_dict, bookings_list, new_booking):
    pass


def under_booked(room_dict, bookings_list, percentage):
    pass


def save_bookings(bookings_list, file_name):
    pass


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

room_data = load_rooms('simple_rooms.csv')
booking_data = load_bookings('simple_bookings.tsv')

print(remove_booking(booking_data, "AHB1B02", "2026-03-03", 11))
