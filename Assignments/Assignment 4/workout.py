# Name: James Jenkins
# Student #: 251491498
# Username: jjenki48
# Date: 31/03/2026
# Description: Defines the Workout class, which represents a single
#              workout session containing a playlist and vital readings.

from song import Song
from vitals import Vitals

class Workout:

    def __init__(self, session_id, date):
        # Initialises session_id and date.
        # _playlist and _log start as empty lists.

        self._session_id = session_id
        self._date = date
        self._playlist = []
        self._log = []

    def get_session_id(self):
        return self._session_id

    def get_date(self):
        return self._date

    def get_playlist(self):
        # Returns a copy of the playlist.
        return self._playlist

    def get_log(self):
        # Returns a copy of the vitals log.
        return self._log

    def add_song(self, song):
        self._playlist.append(song)

    def add_vital(self, vitals):
        self._log.append(vitals)

    def get_average_heart_rate(self):
        # Returns the average heart rate, or None if the log is empty.

        sum_rate = 0

        if self._log == []:
            return None

        for vital in self._log:
            sum_rate += vital.get_heart_rate()
    

        return sum_rate / len(self._log)

    def get_unique_genres(self):
        # Returns a set of unique genre strings from the playlist.
        genres_set = set()

        for song in self._playlist:
            genres_set.add(song.get_genre())    

        return genres_set

    def get_abnormal_readings(self):
        # Returns a list of Vitals objects for which is_abnormal() is True.
        abnormalities = []

        for vital in self._log:
            if vital.is_abnormal():
                abnormalities.append(vital)

        return abnormalities

    def get_segments(self):
        # Divides the vitals log into equal segments, one per song.
        # Returns a list of (Song, [Vitals]) tuples.
        # Returns None if the playlist or log is empty.
        # Divides the vitals log into equal segments, one per song.
        # Returns None if the playlist or log is empty.
      
        if not self._playlist or not self._log:
            return None

        n_songs = len(self._playlist)
        n_readings = len(self._log)
        
        # Calculate base size and the remainder to distribute.
        base_size = n_readings // n_songs
        remainder = n_readings % n_songs
        
        segmentation = []
        current_pos = 0
        
        for i in range(n_songs):
            # First 'remainder' songs receive one extra reading.
            size = base_size + (1 if i < remainder else 0)
            
            # Slice the log to group Vitals into a list for this Song[cite: 405, 664].
            segment_vitals = self._log[current_pos : current_pos + size]
            segmentation.append((self._playlist[i], segment_vitals))
            
            current_pos += size
            
        return segmentation
    
    def get_peak_heart_rate_song(self):
        # Returns the Song with the highest average HR segment (see Part 5).
        # Returns None if playlist or log is empty. 

        info = self.get_segments()

        if not info:
            return None

        peak_song = None
        highest_avg = -1

        for song, segment in info:
            # Compute the average heart rate for this specific segment.
            total_hr = sum(v.get_heart_rate() for v in segment)
            avg_hr = total_hr / len(segment)

            if avg_hr > highest_avg:
                highest_avg = avg_hr
                peak_song = song

        return peak_song

    def __str__(self):
        # Format: "<session_id> on <date>: <n> songs, <n> readings"
        return f"{self._session_id} on {self._date}: {len(self._playlist)} songs, {len(self._log)} readings"

    def __repr__(self):
        return f"Workout('{self._session_id}', {self._date})"

    def __eq__(self, other):
        # Two Workouts are equal if their session_id matches.
        return self._session_id == other._session_id
