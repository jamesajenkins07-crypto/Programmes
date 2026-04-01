# Name:
# Student #:
# Username:
# Date:
# Description: Defines the Patient class, which represents a clinic patient
#              and owns a collection of Workout objects.

from workout import Workout

class Patient:

    def __init__(self, patient_id, name, age, conditions):
        # Initialises all attributes.
        # conditions must be stored as a set.
        pass

    def get_patient_id(self):
        pass

    def get_name(self):
        pass

    def get_age(self):
        pass

    def get_conditions(self):
        # Returns a copy of the conditions set.
        pass

    def get_sessions(self):
        # Returns a copy of the sessions dictionary.
        pass

    def set_name(self, name):
        pass

    def set_age(self, age):
        # Raises ValueError if age is not a positive integer.
        pass

    def add_condition(self, condition):
        pass

    def remove_condition(self, condition):
        pass

    def add_session(self, session):
        pass

    def get_session(self, session_id):
        # Returns the Workout with the given session_id, or None.
        pass

    def get_overall_avg_heart_rate(self):
        # Returns the average HR across all readings in all sessions, or None.
        pass

    def get_heart_rate_trend(self):
        # Returns a sorted list of (date, avg_heart_rate) tuples.
        # Sessions with no vitals are skipped.
        pass

    def get_worst_session(self):
        # Returns the session with the most abnormal readings.
        # Returns None if no sessions exist.
        pass

    def get_top_genre(self):
        # Returns the most frequent genre across all sessions, or None.
        pass

    def __str__(self):
        # Format: "<name> (<id>) | Age: <age> | Conditions: <conditions>"
        # Conditions sorted alphabetically and separated by commas.
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        # Two Patients are equal if their patient_id matches.
        pass
