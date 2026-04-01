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
    

        return sum_rate / len(self.log)

    def get_unique_genres(self):
        # Returns a set of unique genre strings from the playlist.
        genres_list = []

        for song in self._playlist:
            genre = song.get_genre()
            if genre not in genres_list:
                genres_list.append(genre)    
            else:
                genres_list.remove(genre)

    def get_abnormal_readings(self):
        # Returns a list of Vitals objects for which is_abnormal() is True.
        abnormalities = []

        for vital in self._log:
            if log.is_abnormal():
                abnormalities.append(vital)

        return abnormalities

    def get_segments(self):
        # Divides the vitals log into equal segments, one per song.
        # Returns a list of (Song, [Vitals]) tuples.
        # Returns None if the playlist or log is empty.
            
        if not self._playlist or not self._log:
            return None

        if len(self._playlist) == len(self._log):
            return list(zip(self._playlist, self._log))
        
        else:
            segmentation = []
            segment_size = len(self._log) / len(self._playlist)
            
            for i, vital in enumerate(vitals):
                song_index = int(i/segment_size)

                if song_index >= len(songs):
                    song_index = len(songs) - 1
                
                segmentation.append((vital, songs[song_index]))
        
        return segmentation


    def get_peak_heart_rate_song(self):
        # Returns the Song with the highest average HR segment (see Part 5).
        # Returns None if playlist or log is empty. 

        info = self.get_segments()
        
        for tune in info:
            rate = tune[1].get_heart_rate()

            if rate > top_rate:
                top_rate = rate
                song = tune[0]

        return song

    def __str__(self):
        # Format: "<session_id> on <date>: <n> songs, <n> readings"
        return f"{self._session_id} on {self._date}: {len(self._playlist)} songs, {len(self._log)} readings"

    def __repr__(self):
        return f"Workout('{self._session_id}', {self._date})"

    def __eq__(self, other):
        # Two Workouts are equal if their session_id matches.
        return self._session_id == other._session_id
