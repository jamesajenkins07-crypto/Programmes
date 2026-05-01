# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 08/04/2026
# Description: Main program for the Workout Vital Signs Tracker.

from clinic import Clinic
from song import Song
from vitals import Vitals
from workout import Workout
from patient import Patient


# Description: Displays the menu and prompts the user for a valid selection.
# Parameters: None
# Returns: selection (int)
def get_menu_selection():
    print("Select an option:")
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
        selection = input("\nInput selection (1-14): \n").strip()

        if selection.isdigit() and 1 <= int(selection) <= 14:
            return int(selection)
        else:
            print("Invalid input. Try again.")


# Description: Prompts the user for a patient ID and returns the corresponding Patient object if it exists.
# Parameters: patient_id (string)
# Returns: Patient object if found, None otherwise
def valid_patient(patient_id):
    try:
        return clinic.get_patient(patient_id)
    except ValueError:
        print(f"Error: Patient not found: {patient_id}")
        return None


clinic = Clinic("FitTrack Clinic")

while True:
    selection = get_menu_selection()

    # Option 1: Load patients from CSV file
    if selection == 1:
        file_name = input("Enter CSV file name: ").strip()
        try:
            clinic.load_csv(file_name)
            print(f"Patients loaded from {file_name}.")

        except FileNotFoundError:
            print(f"Error: File not found: {file_name}")
            continue

    # Option 2: Add a new patient
    elif selection == 2:
        patient_id = input("Enter patient ID: ").strip()
        name = input("Enter patient name: ").strip()
        age = input("Enter patient age: ").strip()
        conditions_input = input("Enter conditions (comma-separated, or leave blank): \n").strip()
        conditions = set()

        if conditions_input:
            for c in conditions_input.split(","):
                if c.strip():
                    conditions.add(c.strip())

        try:
            patient = Patient(patient_id, name, age, conditions)
            clinic.add_patient(patient)
            print(f"Patient added: {patient}")
        except ValueError as e:
            print(f"Error: Patient not found: {patient_id}")
            continue

    # Option 3: Add a workout session to a patient
    elif selection == 3:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        date = input("Enter session date (YYYY-MM-DD): ").strip()

        try:
            session = Workout(session_id, date)
        except ValueError as e:
            print(e)
            continue

        patient = valid_patient(patient_id)

        if not patient:
            continue

        patient.add_session(session)
        print(f"Session added: {session}")

    # Option 4: Add a song to a session playlist
    elif selection == 4:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        title = input("Enter song title: ").strip()
        artist = input("Enter artist name: ").strip()
        bpm = input("Enter BPM: ").strip()
        genre = input("Enter genre: ").strip()

        try:
            song = Song(title, artist, bpm, genre)
        except ValueError as e:
            print(e)
            continue

        patient = valid_patient(patient_id)

        if not patient:
            continue

        session = patient.get_session(session_id)
        session.add_song(song)

        print(f"Song added: {song}")

    # Option 5: Log a vital reading for a session
    elif selection == 5:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()

        try:
            heart_rate = int(input("Enter heart rate: ").strip())
            systolic = float(input("Enter systolic BP: ").strip())
            diastolic = float(input("Enter diastolic BP: ").strip())
            o2 = float(input("Enter 02 saturation: ").strip())
        except ValueError:
            print("Invalid numeric input. Please enter numbers for vitals.")
            continue

        timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM): ").strip()

        try:
            vital = Vitals(heart_rate, (systolic, diastolic), o2, timestamp)
        except ValueError as e:
            print(e)
            print("Vital reading not added.")
            continue

        patient = valid_patient(patient_id)

        if not patient:
            continue
        try:
            session = patient.get_session(session_id)
        except KeyError:
            print(f"Error: Session not found: {session_id}")
            continue

        session.add_vital(vital)
        print("Vital reading added.")

    # Option 6: View all patients
    elif selection == 6:
        patients_list = clinic.get_patients()

        for patient in patients_list:
            print(clinic.get_patient(patient))

    # Option 7: View sessions for a patient
    elif selection == 7:
        patient_id = input("Enter patient ID: ").strip()
        patient = valid_patient(patient_id)

        if not patient:
            continue

        patient_sessions = patient.get_sessions()

        for session in patient_sessions:
            print(patient_sessions[session])

    # Option 8: View abnormal readings for a session
    elif selection == 8:
        patient_id = input("Enter patient ID: ").strip()
        session_id = input("Enter session ID: ").strip()
        patient = valid_patient(patient_id)

        if not patient:
            continue

        try:
            session = patient.get_session(session_id)
        except KeyError:
            print(f"Error: Session not found: {session_id}")
            continue

        readings = session.get_abnormal_readings()

        if not readings:
            print("No abnormal readings in this session.")
        else:
            for vital in readings:
                print(vital)

    # Option 9: View a patient heart rate trend
    elif selection == 9:
        patient_id = input("Enter patient ID: ").strip()
        patient = valid_patient(patient_id)

        if not patient:
            continue

        readings = patient.get_heart_rate_trend()

        if not readings:
            print(f"No readings available for {patient.get_name()}")
        else:
            for reading in readings:
                print(f"{reading[0]}: {round(reading[1], 1)} bpm")

    # Option 10: View all conditions in the clinic
    elif selection == 10:
        conditions = clinic.get_all_conditions()

        if not conditions:
            print("No conditions recorded in the clinic")
        else:
            print(f"All conditions in the clinic: {conditions}")

    # Option 11: View patients with all of a set of conditions
    elif selection == 11:
        conditions_input = input("Enter conditions separated by commas: \n").strip()
        conditions = {c.strip() for c in conditions_input.split(",") if c.strip()}

        if not conditions:
            print("No conditions entered.")
            continue

        if len(conditions) == 1:
            patients = clinic.get_patients_with_condition(list(conditions)[0])
        else:
            patients = clinic.get_patients_with_conditions(conditions)

        print(f"Patients with all of {conditions}: {patients}")

    # Option 12: View clinic-wide genre heart rate averages
    elif selection == 12:
        averages = clinic.get_genre_hr_averages()

        if not averages:
            print("No data available.")
        else:
            print("Clinic-wide genre heart rate averages:")
            for avg in averages:
                print(f"{avg}: {averages[avg]} bpm")

    # Option 13: Export patient report to .txt file
    elif selection == 13:
        patient_id = input("Enter patient ID: ").strip()
        patient = valid_patient(patient_id)

        if not patient:
            continue

        file_name = f"report_{patient_id}.txt"

        try:
            clinic.export_patient_report(patient_id, file_name)
            print(f"Report exported to {file_name}.")
        except ValueError as e:
            print(e)

    # Option 14: Quit
    elif selection == 14:
        print("\nGoodbye!")
        break
