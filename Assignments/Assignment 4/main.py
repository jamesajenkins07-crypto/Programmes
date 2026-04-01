# Name:
# Student #:
# Username:
# Date:
# Description: Main program for the Workout Vital Signs Tracker.

from clinic import Clinic
from song import Song
from vitals import Vitals
from workout import Workout
from patient import Patient


def get_menu_selection():
    print("\nSelect an option:")
    print(" 1) Import patients from a CSV file")
    print(" 2) Add a new patient")
    print(" 3) Add a workout session to a patient")
    print(" 4) Add a song to a session playlist")
    print(" 5) Log a vital reading for a session")
    print(" 6) View all patients")
    print(" 7) View sessions for a patient")
    print(" 8) View abnormal readings for a session")
    print(" 9) View a patient heart rate trend")
    print("10) View all conditions in the clinic")
    print("11) View patients with all of a set of conditions")
    print("12) View clinic-wide genre heart rate averages")
    print("13) Export patient report to .txt file")
    
    print("14) Quit")
    while True:
        selection = input("\nInput selection (1-15): ").strip()
        if selection.isdigit() and 1 <= int(selection) <= 14:
            return int(selection)
        else:
            print("Invalid input. Try again.")


clinic = Clinic("FitTrack Clinic")

while True:
    selection = get_menu_selection()

    if selection == 1:
        file_name = input("Enter filename: ").strip()
        # You must call load the csv here
        # Catch the error if the file isn't found


    elif selection == 2:
        patient_id = input("Enter patient ID: ").strip()
        name = input("Enter patient name: ").strip()
        age = input("Enter patient age: ").strip()
        conditions_input = input("Enter conditions (comma-separated, or leave blank): ").strip()
        conditions = set()
        if conditions_input:
            for c in conditions_input.split(","):
                if c.strip():
                    conditions.add(c.strip())
        # Create the Patient and add them to the clinic
        # Catch ValueErrors
        # Output should match examples from the assignment sheet


    elif selection == 3:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        date = input("Enter session date (YYYY-MM-DD): ").strip()
        # Find the patient associated with the clinic
        # Add the new Workout session to the patient
        # Catch ValueErrors
        # Output should match examples from the assignment sheet


    elif selection == 4:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        title = input("Enter song title: ").strip()
        artist = input("Enter artist name: ").strip()
        bpm = input("Enter BPM: ").strip()
        genre = input("Enter genre: ").strip()
        # Find the patient associated with the clinic
        # Find the session associated with the patient
        # Add the new Song to the session
        # Catch ValueErrors
        # Output should match examples from the assignment sheet 


    elif selection == 5:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        heart_rate = input("Enter heart rate: ").strip()
        systolic = input("Enter systolic BP: ").strip()
        diastolic = input("Enter diastolic BP: ").strip()
        o2 = input("Enter O2 saturation: ").strip()
        timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM): ").strip()
        # Find the patient associated with the clinic
        # Find the session associated with the patient
        # Add the new Vital to the session
        # Catch ValueErrors
        # Output should match examples from the assignment sheet 


    elif selection == 6:
        # Print off all patients from the clinic
        # If there aren't any, print "No patients in the clinic."
        pass

    elif selection == 7:
        patient_id = input("Enter patient ID: ").strip()
        # Find the patient associated with the clinic
        # Find all the session(s) associated with the patient
        # Catch ValueErrors
        # Output should match examples from the assignment sheet


    elif selection == 8:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        # Find the patient associated with the clinic
        # Find the session associated with the patient 
        # Catch ValueErrors
        # Output should match example from the assignment sheet if no abnormal readings
        # Output should show all abnormal readings if there are any


    elif selection == 9:
        patient_id = input("Enter patient ID: ").strip()
        # Find the patient associated with the clinic
        # Find the patient's heart rate trend
        # Catch ValueErrors
        # If there are no readings, print "No readings available for <patient name>."
        # Otherwise, output should show the heart rate trend as in the assignment sheet


    elif selection == 10:
        # Print all of the conditions associated with the clinic as in the example from the assignment sheet
        # If no conditions, print "No conditions recorded in the clinic."
        pass

    elif selection == 11:
        conditions_input = input("Enter conditions separated by commas: ").strip()
        # Print all of the patients with the conditions
        pass

    elif selection == 12:
        # If there is no data, print "No genre data available."
        # Otherwise, print the averages by genre as in the example from the assignment sheet
        pass

    elif selection == 13:
        patient_id = input("Enter patient ID: ").strip()
        file_name = "report_" + patient_id + ".txt"
        # Export the patient's information to a txt file
        # Catch ValueErrors

    elif selection == 14:
        print("Goodbye!")
        break
