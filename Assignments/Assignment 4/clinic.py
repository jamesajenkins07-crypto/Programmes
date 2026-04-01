# Name:
# Student #:
# Username:
# Date:
# Description: Defines the Clinic class, which manages the full patient
#              roster and handles all file input and output.

import csv
from patient import Patient
from workout import Workout
from song import Song
from vitals import Vitals

class Clinic:

    def __init__(self, name):
        pass

    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_patients(self):
        # Returns a copy of the patients dictionary.
        pass

    def add_patient(self, patient):
        pass

    def get_patient(self, patient_id):
        # Returns the Patient with the given ID.
        # Raises ValueError if not found.
        pass

    def search_patients_by_name(self, name):
        # Returns a list of Patients whose name contains the given string
        # (case-insensitive, partial match).
        pass

    def get_patients_with_condition(self, condition):
        # Returns a set of patient_id strings for patients who have this condition.
        pass

    def get_all_conditions(self):
        # Returns the union of all patients' condition sets.
        pass

    def get_patients_with_conditions(self, conditions):
        # Returns a set of patient_id strings for patients whose conditions
        # set contains ALL of the given conditions (superset check).
        pass

    def get_highest_avg_hr_patient(self):
        # Returns the Patient with the highest overall average heart rate, or None.
        pass

    def get_genre_hr_averages(self):
        # Returns a dict mapping genre to average HR across the whole clinic.
        # Uses the positional approximation from Part 5.
        pass

    def load_csv(self, file_name):
        # Reads the CSV file and populates the clinic.
        # Catches ValueError, prints a message, and continues.
        pass

    def export_patient_report(self, patient_id, file_name):
        # Exports a plain text report for the given patient.
        # Raises ValueError if the patient does not exist.
        pass

    def __str__(self):
        # Format: "<name> | <n> patients"
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        # Two Clinics are equal if their name matches.
        pass
