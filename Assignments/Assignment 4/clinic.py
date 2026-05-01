# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 07/04/2026
# Description: Defines the Clinic class, which manages the full patient
#              roster and handles all file input and output.

import csv
from patient import Patient
from workout import Workout
from song import Song
from vitals import Vitals


class Clinic:

    # Description: Initialises a new Clinic instance with the given name and an empty patient roster.
    # Parameters: name (string)
    # Returns: None
    def __init__(self, name):
        self._name = name
        self._patients = {}

    # Description: Returns the clinic's name.
    # Parameters: None
    # Returns: name (string)
    def get_name(self):
        return self._name

    # Description: Sets the clinic's name.
    # Parameters: name (string)
    # Returns: None
    def set_name(self, name):
        self._name = name

    # Description: Returns a copy of the clinic's patients dictionary.
    # Parameters: None
    # Returns: patients (dict of patient_id: Patient)
    def get_patients(self):
        return self._patients.copy()

    # Description: Adds a patient to the clinic's roster.
    # Parameters: patient (Patient)
    # Returns: None
    def add_patient(self, patient):
        self._patients[patient.get_patient_id()] = patient

    # Description: Returns the Patient with the given ID.
    # Parameters: patient_id (string)
    # Returns: Patient with the given ID, or raises ValueError if not found.
    def get_patient(self, patient_id):
        if patient_id in self._patients:
            return self._patients[patient_id]
        else:
            raise ValueError(f"Patient not found: {patient_id}")

    # Description: Searches for patients by name.
    # Parameters: name (string)
    # Returns: A list of Patients whose name contains the given string (case-insensitive, partial match).
    def search_patients_by_name(self, name):
        possible_patients = []

        for patient in self._patients:
            patient_name = self._patients[patient].get_name()

            if name.lower() in patient_name.lower():
                possible_patients.append(self._patients[patient])

        return possible_patients

    # Description: Returns a set of patient_id strings for patients who have the given condition.
    # Parameters: condition (string)
    # Returns: A set of patient_id strings for patients whose conditions set
    # contains the given condition (case-insensitive, exact match).
    def get_patients_with_condition(self, condition):
        possible_patients = []

        for patient in self._patients:
            if condition in self._patients[patient].get_conditions():
                possible_patients.append(self._patients[patient].get_patient_id())

        return set(possible_patients)

    # Description: Returns a set of all conditions that patients in the clinic have.
    # Parameters: None
    # Returns: A set of all conditions that patients in the clinic have.
    def get_all_conditions(self):
        total = set()

        for patient in self._patients:
            total.update(self._patients[patient].get_conditions())

        return total

    # Description: Returns a set of patient_id strings for patients who have all of the given conditions.
    # Parameters: conditions (set of strings)
    # Returns: A set of patient_id strings for patients whose conditions set is a superset
    def get_patients_with_conditions(self, conditions):
        possible_patients = []

        for patient in self._patients.values():
            if patient.get_conditions().issuperset(conditions):
                possible_patients.append(patient.get_patient_id())

        return set(possible_patients)

    # Description: Returns the Patient with the highest overall average heart rate across all sessions.
    # Parameters: None
    # Returns: The Patient with the highest overall average heart rate across all sessions, or None
    def get_highest_avg_hr_patient(self):
        max_patient = None
        max_hr = 0

        for patient in self._patients.values():
            hr = patient.get_overall_avg_heart_rate()

            if hr is not None:
                if hr > max_hr:
                    max_hr = hr
                    max_patient = patient

        return max_patient

    # Description: Returns a dictionary mapping each genre to the average heart rate across all segments of that genre.
    # Parameters: None
    # Returns: A dictionary mapping each genre to the average heart rate across all segments of that
    def get_genre_hr_averages(self):
        genre_totals = {}

        for patient in self._patients.values():
            for workout in patient.get_sessions().values():

                if not workout.get_segments():
                    continue

                for song, segment_vitals in workout.get_segments():
                    genre = song.get_genre()

                    segment_hr_sum = sum(v.get_heart_rate() for v in segment_vitals)
                    segment_avg = segment_hr_sum / len(segment_vitals)

                    if genre not in genre_totals:
                        genre_totals[genre] = [segment_avg]
                    else:
                        genre_totals[genre].append(segment_avg)

        for genre in genre_totals:
            genre_totals[genre] = round((sum(genre_totals[genre]) / len(genre_totals[genre])), 1)

        return genre_totals

    # Description: Loads patient, session, song, and vital data from a CSV file and populates the clinic's roster.
    # Parameters: file_name (string)
    # Returns: None
    def load_csv(self, file_name):
        with open(file_name, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record_type = row["record_type"].strip()
                patient_id = row["patient_id"].strip()

                if record_type == "patient":
                    name = row["name"].strip()
                    age = int(row["age"].strip())
                    cond_str = row["conditions"].strip()
                    conditions = set()

                    for c in cond_str.split("|"):
                        if c.strip() != "":
                            conditions.add(c.strip())

                    new_patient = Patient(patient_id, name, age, conditions)
                    self.add_patient(new_patient)

                if record_type == "session":
                    workout_id = row["session_id"].strip()
                    date = row["date"].strip()
                    session = Workout(workout_id, date)
                    self._patients[patient_id].add_session(session)

                if record_type == "song":
                    title = row["title"].strip()
                    workout_id = row["session_id"].strip()
                    artist = row["artist"].strip()
                    bpm = row["bpm"].strip()
                    genre = row["genre"].strip()
                    song = Song(title, artist, int(bpm), genre)
                    self._patients[patient_id].get_session(workout_id).add_song(song)

                if record_type == "vital":
                    workout_id = row["session_id"].strip()
                    hr = row["heart_rate"].strip()
                    bp_sys = row["bp_systolic"].strip()
                    bp_dia = row["bp_diastolic"].strip()
                    o2_sat = row["o2_saturation"].strip()
                    timestamp = row["timestamp"].strip()

                    try:
                        vital = Vitals(float(hr), (int(bp_sys), int(bp_dia)), float(o2_sat), timestamp)
                        self._patients[patient_id].get_session(workout_id).add_vital(vital)
                    except ValueError as e:
                        print(f"Skipping invalid vital reading for {patient_id} ({workout_id}, {timestamp}")
                        continue

    # Description: Exports a patient report to a text file with the given name.
    # Parameters: patient_id (string), file_name (string)
    # Returns: None
    def export_patient_report(self, patient_id, file_name):
        try:
            patient = self._patients[patient_id]
        except KeyError:
            raise ValueError("Patient does not exist!")

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"{self._name.upper()} CLINIC — PATIENT REPORT")
            f.write(f"Patient: {patient.get_name()}\n")
            f.write(f"ID: {patient_id}\n")
            f.write(f"Age: {patient.get_age()}\n")
            f.write(f"Conditions: {", ".join(sorted(patient.get_conditions()))}")
            f.write("\n")
            f.write("-" * 60 + "\n")

            for session in patient.get_sessions().values():
                f.write(f"SESSION: {session.get_session_id()} | Date: {session.get_date()}\n")
                f.write("  Playlist:\n")

                count = 1

                for song in session.get_playlist():
                    f.write(f"\t{count}. {str(song)}\n")
                    count += 1

                f.write(f"  Genres this session: {", ".join(sorted(session.get_unique_genres()))}\n")
                f.write(f"  Average heart rate: {round(session.get_average_heart_rate(), 1)}\n")

                abnormal = session.get_abnormal_readings()

                if not abnormal:
                    abnormal = None

                f.write(f"  Abnormal readings: {abnormal}\n")
                f.write("\n")

            f.write("\n")
            f.write("-" * 60 + "\n")
            f.write("SUMMARY\n")
            f.write("-" * 60 + "\n")

            f.write(f"Overall average heart rate: {round(patient.get_overall_avg_heart_rate(), 1)} bpm\n")
            f.write(f"Most frequent genre: {patient.get_top_genre()}\n")
            f.write(f"Worst session (most abnormal readings): {patient.get_worst_session()}\n")
            f.write("\n")
            f.write("Heart rate trend (oldest to newest):\n")

            for trend in patient.get_heart_rate_trend():
                f.write(f"{trend[0]}: {round(trend[1], 1)} bpm\n")

            f.write("=" * 60 + "\n")

    # Description: Returns a string representation of the clinic.
    # Parameters: None
    # Returns: string in format "<name> | <n> patients"
    def __str__(self):
        return f"{self._name} | {len(self._patients)} patients"

    # Description: Returns a string representation of the clinic for debugging.
    # Parameters: None
    # Returns: string in format "Clinic('<name>')"
    def __repr__(self):
        return f"Clinic({self._name})"

    # Description: Two Clinic instances are equal if they have the same name.
    # Parameters: other (Clinic)
    # Returns: True if self and other have the same name, False otherwise.
    def __eq__(self, other):
        return self._name == other._name
