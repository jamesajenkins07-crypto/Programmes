# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 31/03/2026
# Description: Defines the Workout class, which represents a single
#              workout session containing a playlist and vital readings.

from song import Song
from vitals import Vitals


class Workout:

    # Description: Initialises a new Workout instance with the given values.
    # Parameters: session_id (string), date (string)
    # Returns: None
    def __init__(self, session_id, date):
        self._session_id = session_id
        self._date = date
        self._playlist = []
        self._log = []

    # Description: Returns the session_id string.
    # Parameters: None
    # Returns: session_id (string)
    def get_session_id(self):
        return self._session_id

    # Description: Returns the date string.
    # Parameters: None
    # Returns: date (string)
    def get_date(self):
        return self._date

    # Description: Returns a copy of the playlist.
    # Parameters: None
    # Returns: list of Song objects
    def get_playlist(self):
        return self._playlist.copy()

    # Description: Returns a copy of the vitals log.
    # Parameters: None
    # Returns: list of Vitals objects
    def get_log(self):
        return self._log.copy()

    # Description: Adds a Song to the playlist.
    # Parameters: song (Song)
    # Returns: None
    def add_song(self, song):
        self._playlist.append(song)

    # Description: Adds a Vitals object to the log.
    # Parameters: vitals (Vitals)
    # Returns: None
    def add_vital(self, vitals):
        self._log.append(vitals)

    # Description: Returns the average heart rate across all vitals readings in the log.
    # Parameters: None
    # Returns: average heart rate (float), or None if the log is empty
    def get_average_heart_rate(self):
        sum_rate = 0

        if self._log == []:
            return None

        for vital in self._log:
            sum_rate += vital.get_heart_rate()

        return sum_rate / len(self._log)

    # Description: Returns a set of unique genre strings from the playlist.
    # Parameters: None
    # Returns: set of unique genre strings
    def get_unique_genres(self):
        genres_set = set()

        for song in self._playlist:
            genres_set.add(song.get_genre())

        return genres_set

    # Description: Returns a list of Vitals objects for which is_abnormal() is True.
    # Parameters: None
    # Returns: list of Vitals objects with abnormal readings
    def get_abnormal_readings(self):
        abnormalities = []

        for vital in self._log:
            if vital.is_abnormal():
                abnormalities.append(vital)

        return abnormalities

    # Description: Divides the vitals log into equal segments, one per song.
    # Parameters: None
    # Returns: list of (Song, [Vitals]) tuples, or None if the playlist or log is empty
    def get_segments(self):
        if not self._playlist or not self._log:
            return None

        n_songs = len(self._playlist)
        n_readings = len(self._log)

        base_size = n_readings // n_songs
        remainder = n_readings % n_songs

        segmentation = []
        current_pos = 0

        for i in range(n_songs):
            size = base_size + (1 if i < remainder else 0)
            segment_vitals = self._log[current_pos:current_pos + size]
            segmentation.append((self._playlist[i], segment_vitals))
            current_pos += size

        return segmentation

    # Description: Returns the Song that corresponds to the segment with the
    # highest average heart rate, or None if no segments.
    # Parameters: None
    # Returns: peak_song (Song) or None
    def get_peak_heart_rate_song(self):
        info = self.get_segments()

        if not info:
            return None

        peak_song = None
        highest_avg = -1

        for song, segment in info:
            total_hr = sum(v.get_heart_rate() for v in segment)
            avg_hr = total_hr / len(segment)

            if avg_hr > highest_avg:
                highest_avg = avg_hr
                peak_song = song

        return peak_song

    # Description: Returns a string representation of the workout.
    # Parameters: None
    # Returns: string in format "<session_id> on <date>: <n> songs, <n> readings"
    def __str__(self):
        return f"{self._session_id} on {self._date}: {len(self._playlist)} songs, {len(self._log)} readings"

    # Description: Returns a string representation of the workout for debugging.
    # Parameters: None
    # Returns: string in format "Workout('<session_id>', '<date>')"
    def __repr__(self):
        return f"Workout('{self._session_id}', '{self._date}')"

    # Description: Two Workout instances are equal if they have the same session_id.
    # Parameters: other (Workout)
    # Returns: True if self and other have the same session_id, False otherwise.
    def __eq__(self, other):
        return self._session_id == other._session_id
