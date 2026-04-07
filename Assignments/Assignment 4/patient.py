#!/bin/python3
# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 07/04/2026
# Description: Defines the Patient class, which represents a clinic patient
#              and owns a collection of Workout objects.

from workout import Workout

class Patient:

    def __init__(self, patient_id, name, age, conditions):
        # Initialises all attributes.
        # conditions must be stored as a set.

        self._patient_id = patient_id
        self._name = name
        self._age = age
        self._conditions = conditions
        self._sessions = {}

    def get_patient_id(self):
        return self._patient_id

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_conditions(self):
        # Returns a copy of the conditions set.
        return self._conditions

    def get_sessions(self):
        # Returns a copy of the sessions dictionary.
        return self._sessions

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        # Raises ValueError if age is not a positive integer.
        if age > 0:
            self._age = age
        else:
            raise ValueError("Age must be positive integer")

    def add_condition(self, condition):
        self._conditions.add(condition)

    def remove_condition(self, condition):
        self._conditions.discard(condition)

    def add_session(self, session):
        self._sessions[session.get_session_id()] = session

    def get_session(self, session_id):
        # Returns the Workout with the given session_id, or None.
        if session_id in self._sessions:
            return self._sessions[session_id]
        else:
            None

    def get_overall_avg_heart_rate(self):
        # Returns the average HR across all readings in all sessions, or None.
        all_readings = []

        for session in self._sessions.values():
            for vital in session.get_log():
                all_readings.append(vital.get_heart_rate())

        if not all_readings:
            return None
        return sum(all_readings) / len(all_readings)

    def get_heart_rate_trend(self):
        # Returns a sorted list of (date, avg_heart_rate) tuples.
        # Sessions with no vitals are skipped.
        sorted_trend = []

        if not self._sessions:
            return None
        
        for session in self._sessions:
            date = self._sessions[session].get_date()
            vitals = self._sessions[session].get_average_heart_rate()
            
            if vitals:
                sorted_trend.append((date, vitals))
            else:
                continue
        
        return sorted_trend

    def get_worst_session(self):
        # Returns the session with the most abnormal readings.
        # Returns None if no sessions exist.
        if not self._sessions:
            return None
        
        amount_abnormalities = 0

        for session in self._sessions:
            odd_ones = self._sessions[session].get_abnormal_readings()
            if len(odd_ones) > amount_abnormalities:
                worst = self._sessions[session]
                amount_abnormalities = len(worst.get_abnormal_readings())

        return worst

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

        if count == {}:
            return None
        else:
            return max(count, key=count.get)            

    def __str__(self):
        # Format: "<name> (<id>) | Age: <age> | Conditions: <conditions>"
        # Conditions sorted alphabetically and separated by commas.
        return f"{self._name} ({self._patient_id}) | Age: {self._age} | Conditions: {", ".join(sorted(self.get_conditions()))}"

    def __repr__(self):
        return f"Patient({self._patient_id}, {self._name}, {self._age}, {self._conditions})"

    def __eq__(self, other):
        # Two Patients are equal if their patient_id matches.
        return self._patient_id == other._patient_id
