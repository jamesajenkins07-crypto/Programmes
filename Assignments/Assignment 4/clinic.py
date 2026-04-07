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

    def __init__(self, name):
        self._name = name
        self._patients = {}

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_patients(self):
        # Returns a copy of the patients dictionary.
        return self._patients

    def add_patient(self, patient):
        self._patients[patient.get_patient_id()] = patient

    def get_patient(self, patient_id):
        # Returns the Patient with the given ID.
        # Raises ValueError if not found.
        if patient_id in self._patients:
            return self._patients[patient_id]
        else:
            raise ValueError(f"Patient not found: {patient_id}")

    def search_patients_by_name(self, name):
        # Returns a list of Patients whose name contains the given string
        # (case-insensitive, partial match).
        
        possible_patients = []

        for patient in self._patients:
            patient_name = self._patients[patient].get_name()
        
            if name.lower() in patient_name.lower():
                possible_patients.append(self._patients[patient])

        return possible_patients

    def get_patients_with_condition(self, condition):
        # Returns a set of patient_id strings for patients who have this condition.
        possible_patients = []
        
        for patient in self._patients:
            if condition in self._patients[patient].get_conditions():
                possible_patients.append(self._patients[patient].get_patient_id())
        
        return set(possible_patients)

    def get_all_conditions(self):
        # Returns the union of all patients' condition sets.
        total = set()
        for patient in self._patients:
            total.update(self._patients[patient].get_conditions())

        return total

    def get_patients_with_conditions(self, conditions):
        # Returns a set of patient_id strings for patients whose conditions
        # set contains ALL of the given conditions (superset check).
        possible_patients = []
        for patient in self._patients.values():
            if patient.get_conditions().issuperset(conditions):
                possible_patients.append(patient.get_patient_id())

        return set(possible_patients)

    def get_highest_avg_hr_patient(self):
        # Returns the Patient with the highest overall average heart rate, or None.
        max_hr = 0
        for patient in self._patients.values():
            hr = patient.get_overall_avg_heart_rate()
            if max_hr < hr:
                max_hr = hr
                max_patient = patient
        return max_patient

    def get_genre_hr_averages(self):
        # Returns a dict mapping genre to average HR across the whole clinic.
        # Uses the positional approximation from Part 5.
        genre_totals = {}

        for patient in self._patients.values():
            for workout in patient.get_sessions().values():

                if not workout.get_segments():
                    continue

                for song, vital in workout.get_segments():
                    genre = song.get_genre()
                    if genre not in genre_totals:
                        genre_totals[genre] = [vital[0].get_heart_rate()]
                    else:
                        genre_totals[genre].append(vital[0].get_heart_rate())
        
        for genre in genre_totals:
            genre_totals[genre] = sum(genre_totals[genre]) / len(genre_totals[genre])

        return genre_totals

    def load_csv(self, file_name):
        # Reads the CSV file and populates the clinic.
        # Catches ValueError, prints a message, and continues.
        
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
                        print(f"Skipped invalid reading for {patient_id} ({workout_id}, {timestamp}: {e}")
                        continue

    def export_patient_report(self, patient_id, file_name):
        # Exports a plain text report for the given patient.
        # Raises ValueError if the patient does not exist.
        
        try:
            patient = self._patients[patient_id]
        except KeyError:
            raise ValueError("Patient does not exist!")
        
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"Patient: {patient.get_name()}\n")
            f.write(f"Age: {patient.get_age()}\n")
            f.write(f"Conditions: {", ".join(sorted(patient.get_conditions()))}")
            f.write("\n")
            f.write("-" * 60 + "\n")
        
        for session in patient.get_sessions().values():
            f.write(f"SESSION: {session.get_session_id()}  |  Date: {session.get_date()}\n")
            f.write("\n")
            f.write("  Playlist:")
            
            count = 1
            for song in session.get_playlist():
                f.write(f"{count}. {str(song)}")
            
            f.write(f"Genres this session: {", ".join(sorted(session.get_unique_genres()))}\n")
            f.write(f"Average heart rate: {session.get_average_heart_rate()}\n")
            f.write(f"Abnormal readings: {session.get_abnormal_readings()}\n")
            f.write("\n")
        
        f.write("\n")
        f.write("-" * 60 + "\n")
        f.write("SUMMARY")
        f.write("-" * 60 + "\n")

        f.write(f"Overall average heart rate: {patient.get_overall_avg_heart_rate()} bpm")
        f.write(f"Most frequent genre: {patient.get_top_genre()}")
        f.write(f"Worst session (most abnormal readings): {patient.get_worst_session()}")
        f.write("\n")
        f.write("Heart rate trend (oldest to newest):\n")

        for trend in patient.get_heart_rate_trend():
            f.write(f"{trend[0]}: {trend[1]} bpm")

        f.write("=" * 60 + "\n")

    def __str__(self):
        # Format: "<name> | <n> patients"
        return f"{self._name} | {len(self._patients)} patients"

    def __repr__(self):
        return f"Clinic({self._name})"

    def __eq__(self, other):
        return self._name == other._name
