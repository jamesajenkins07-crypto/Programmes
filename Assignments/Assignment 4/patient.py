#!/bin/python3
# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 07/04/2026
# Description: Defines the Patient class, which represents a clinic patient
#              and owns a collection of Workout objects.

from workout import Workout


class Patient:

    # Description: Initialises a new patient instance
    # Parameters: patient_id (string), name (string), age (int), conditions (set of strings)
    # Returns: None
    def __init__(self, patient_id, name, age, conditions):
        self._patient_id = patient_id
        self._name = name
        self._age = age
        self._conditions = set(conditions)
        self._sessions = {}

    # Description: Returns the patient_id string.
    # Parameters: None
    # Returns: patient_id (string)
    def get_patient_id(self):
        return self._patient_id

    # Description: Returns the patient's name.
    # Parameters: None
    # Returns: name (string)
    def get_name(self):
        return self._name

    # Description: Returns the patient's age.
    # Parameters: None
    # Returns: age (int)
    def get_age(self):
        return self._age

    # Description: Returns a copy of the patient's conditions set.
    # Parameters: None
    # Returns: conditions (set of strings)
    def get_conditions(self):
        return self._conditions.copy()

    # Description: Returns a copy of the patient's sessions dictionary.
    # Parameters: None
    # Returns: sessions (dict of session_id: Workout)
    def get_sessions(self):
        return self._sessions.copy()

    # Description: Sets the patient's name.
    # Parameters: name (string)
    # Returns: None
    def set_name(self, name):
        self._name = name

    # Description: Sets the patient's age.
    # Parameters: age (int)
    # Returns: None
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError("Age must be positive integer")

    # Description: Adds a condition to the patient's conditions set.
    # Parameters: condition (string)
    # Returns: None
    def add_condition(self, condition):
        self._conditions.add(condition)

    # Description: Removes a condition from the patient's conditions set.
    # Parameters: condition (string)
    # Returns: None
    def remove_condition(self, condition):
        self._conditions.discard(condition)

    # Description: Adds a workout session to the patient's sessions dictionary.
    # Parameters: session (Workout)
    # Returns: None
    def add_session(self, session):
        self._sessions[session.get_session_id()] = session

    # Description: Returns the Workout with the given session_id, or None if not found.
    # Parameters: session_id (string)
    # Returns: session (Workout) or None
    def get_session(self, session_id):
        return self._sessions.get(session_id)

    # Description: Returns the average heart rate across all sessions, or None if no readings.
    # Parameters: None
    # Returns: average_heart_rate (float) or None
    def get_overall_avg_heart_rate(self):
        all_readings = []

        for session in self._sessions.values():
            for vital in session.get_log():
                all_readings.append(vital.get_heart_rate())

        if not all_readings:
            return None

        return sum(all_readings) / len(all_readings)

    # Description: Returns a list of (date, average_heart_rate) tuples sorted by date.
    # Parameters: None
    # Returns: trend (list of (date, average_heart_rate) tuples) or None if no sessions
    def get_heart_rate_trend(self):
        sorted_trend = []

        if not self._sessions:
            return None

        for session in self._sessions:
            date = self._sessions[session].get_date()
            avg_hr = self._sessions[session].get_average_heart_rate()

            if avg_hr:
                sorted_trend.append((date, avg_hr))
            else:
                continue

        return sorted(sorted_trend)

    # Description: Returns the Workout with the most abnormal vital readings, or None if no sessions.
    # Parameters: None
    # Returns: worst_session (Workout) or None
    def get_worst_session(self):
        if not self._sessions:
            return None

        session_ids = list(self._sessions.keys())
        worst = self._sessions[session_ids[0]]
        amount_abnormalities = len(worst.get_abnormal_readings())

        for session_id in self._sessions:
            session = self._sessions[session_id]
            odd_ones = session.get_abnormal_readings()

            if len(odd_ones) > amount_abnormalities:
                worst = session
                amount_abnormalities = len(odd_ones)

        return worst

    # Description: Returns the genre that appears most frequently across all sessions, or None if no sessions.
    # Parameters: None
    # Returns: top_genre (string) or None
    def get_top_genre(self):
        count = {}

        if not self._sessions:
            return None

        for session in self._sessions:
            playlist = self._sessions[session].get_playlist()

            if not playlist:
                continue

            for song in playlist:
                genre = song.get_genre()

                if genre in count:
                    count[genre] += 1
                else:
                    count[genre] = 1

        if not count:
            return None
        else:
            return max(count, key=count.get)

    # Description: Returns a string representation of the patient.
    # Parameters: None
    # Returns: string in format "<name> (<patient_id>) | Age: <age> | Conditions: <condition1>, <condition2>, ..."
    def __str__(self):
        return (f"{self._name} ({self._patient_id}) | " +
                f"Age: {self._age} | Conditions: {', '.join(sorted(self.get_conditions()))}")

    # Description: Returns a string representation of the patient for debugging.
    # Parameters: None
    # Returns: string in format "Patient(<patient_id>, <name>, <age>, <conditions>)"
    def __repr__(self):
        return f"Patient('{self._patient_id}', '{self._name}', {self._age}, {self._conditions})"

    # Description: Two Patients are equal if their patient_id matches.
    # Parameters: other (Patient)
    # Returns: True if self and other have the same patient_id, False otherwise.
    def __eq__(self, other):
        return self._patient_id == other._patient_id
