# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 30/03/2026
# Description: Defines the Vitals class, which represents one set
#              of vital signs recorded during a workout session.

class Vitals:

    # Description: Initialises a new Vitals instance with the given values.
    # Parameters: heart_rate (int), blood_pressure (tuple of two ints), o2_saturation (float), timestamp (string)
    # Returns: None
    def __init__(self, heart_rate, blood_pressure, o2_saturation, timestamp):
        if 1 <= heart_rate <= 300:
            self._heart_rate = heart_rate
        else:
            raise ValueError(f"Invalid heart rate: {heart_rate}. Must be between 1 and 300.")

        if 40 <= blood_pressure[0] <= 300:
            if 20 <= blood_pressure[1] <= 200:
                self._blood_pressure = blood_pressure
            else:
                raise ValueError(f"Invalid diastolic blood pressure: {blood_pressure[1]}. Must be between 20 and 200.")
        else:
            raise ValueError(f"Invalid systolic blood pressure: {blood_pressure[0]}. Must be between 40 and 300.")

        if 50 <= o2_saturation <= 100:
            self._o2_saturation = o2_saturation
        else:
            raise ValueError(f"Invalid 02 saturation: {o2_saturation}. Must be between 50.0 and 100.0.")

        self._timestamp = timestamp

    # Description: Returns the heart rate value.
    # Parameters: None
    # Returns: heart_rate (int)
    def get_heart_rate(self):
        return self._heart_rate

    # Description: Returns the blood pressure value as a tuple (systolic, diastolic).
    # Parameters: None
    # Returns: blood_pressure (tuple of two ints)
    def get_blood_pressure(self):
        return self._blood_pressure

    # Description: Returns the o2 saturation value.
    # Parameters: None
    # Returns: o2_saturation (float)
    def get_o2_saturation(self):
        return self._o2_saturation

    # Description: Returns the timestamp value.
    # Parameters: None
    # Returns: timestamp (string)
    def get_timestamp(self):
        return self._timestamp

    # Description: Determines if the vitals reading is abnormal.
    # Parameters: None
    # Returns: True if any value is outside the normal range, False otherwise.
    def is_abnormal(self):
        if not 60 <= self._heart_rate <= 100:
            return True
        elif not 90 <= self._blood_pressure[0] <= 140:
            return True
        elif not 60 <= self._blood_pressure[1] <= 90:
            return True
        elif self._o2_saturation < 95:
            return True
        else:
            return False

    # Description: Returns a string representation of the vitals reading.
    # Parameters: None
    # Returns: string in format "HR: <hr> bpm | BP: <sys>/<dia> | O2: <o2>% | <timestamp>"
    def __str__(self):
        return (f"HR: {self._heart_rate} bpm | BP: {self._blood_pressure[0]}/" +
                f"{self._blood_pressure[1]} | O2: {self._o2_saturation}% | {self._timestamp}")

    # Description: Returns a string representation of the vitals reading for debugging.
    # Parameters: None
    # Returns: string in format "Vitals(<heart_rate>, <blood_pressure>, <o2_saturation>, '<timestamp>')"
    def __repr__(self):
        return f"Vitals({self._heart_rate}, {self._blood_pressure}, {self._o2_saturation}, '{self._timestamp}')"

    # Description: Two Vitals readings are equal if all four values match.
    # Parameters: other (Vitals)
    # Returns: True if self and other have the same heart rate,
    # blood pressure, o2 saturation, and timestamp, False otherwise.
    def __eq__(self, other):
        return (self._heart_rate == other._heart_rate and
                self._blood_pressure == other._blood_pressure and
                self._o2_saturation == other._o2_saturation and
                self._timestamp == other._timestamp)

    # Description: Compares this Vitals reading to another based on heart rate.
    # Parameters: other (Vitals)
    # Returns: True if this reading's heart rate is lower than the other's, False otherwise
    def __lt__(self, other):
        return self._heart_rate < other._heart_rate

    # Description: Compares this Vitals reading to another based on heart rate.
    # Parameters: other (Vitals)
    # Returns: True if this reading's heart rate is greater than the other's, False otherwise
    def __gt__(self, other):
        return self._heart_rate > other._heart_rate
