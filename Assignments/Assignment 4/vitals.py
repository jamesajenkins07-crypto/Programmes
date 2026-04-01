# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 30/03/2026
# Description: Defines the Vitals class, which represents one set
#              of vital signs recorded during a workout session.

class Vitals:

    def __init__(self, heart_rate, blood_pressure, o2_saturation, timestamp):
        # Validates all values against the valid ranges in Part 3.
        # Raises ValueError if any value is out of range.
        # Check order: heart_rate, systolic BP, diastolic BP, o2_saturation.
        # Then initializes all private attributes.
        # blood_pressure must be stored as a tuple.
        if 1 <= heart_rate <= 300:
            self.heart_rate = heart_rate
        else:
            raise ValueError(f"Invalid heart rate: {heart_rate}. Must be between 1 and 300")

        if 40 <= blood_pressure[0] <= 300:
            self.blood_pressure = blood_pressure
        else:
            raise ValueError(f"Invalid systolic pressure: {blood_pressure[0]}. Must be between 40 and 300.")

        if 20 <= blood_pressure[1] <= 200:
            self.o2_saturation = o2_saturation
        else:
            raise ValueError(f"Invalid diastolic pressure: {blood_pressure[1]}. Must be between 20 and 200.")
        if 50 <= o2_saturation <= 100:
            self.timestamp = timestamp
        else:
            raise ValueError(f"Invalid O2 saturation: {o2_saturation}. Must be between 50.0 and 100.0")

    def get_heart_rate(self):
        return self.heart_rate

    def get_blood_pressure(self):
        return self.blood_pressure

    def get_o2_saturation(self):
        return self.o2_saturation

    def get_timestamp(self):
        return self.timestamp

    def is_abnormal(self):
        # Returns True if any value is outside the normal range (see Part 3).
        if not 60 <= self.heart_rate <= 100:
            return True
        elif not 90 <= self.blood_pressure[0] <= 140:
            return True
        elif not 60 <= self.blood_pressure[1] <= 90:
            return True
        elif not 95 <= self.o2_saturation:
            return True
        else:
            return False
        

    def __str__(self):
        # Returns: "HR: <hr> bpm | BP: <sys>/<dia> | O2: <o2>% | <timestamp>"
        return f"HR: {self.heart_rate} bpm | BP: {self.blood_pressure[0]} / {self.blood_pressure[1]} | O2: {self.o2_saturation}% | {self.timestamp}"

    def __repr__(self):
        return f"Vitals({self.heart_rate}, {self.blood_pressure}, {self.o2_saturation}, '{self.timestamp}')"

    def __eq__(self, other):
        # Returns True if all four values match.
        return self.heart_rate == other.heart_rate and self.blood_pressure == other.blood_pressure and self.o2_saturation == other.o2_saturation and self.timestamp == other.timestamp

    def __lt__(self, other):
        # Returns True if this reading's heart rate is lower than the other's.
        return self.heart_rate < other.heart_rate

    def __gt__(self, other):
        # Returns True if this reading's heart rate is greater than the other's.
        return self.heart_rate > other.heart_rate

