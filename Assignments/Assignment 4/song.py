# Name: James Jenkins
# Student #: 251491498
# Username: jjenki4
# Date: 30/03/2026
# Description: Defines the Song class, which represents a single music
#              track in a workout session playlist.

class Song:

    def __init__(self, title, artist, bpm, genre):
        self.title = title
        self.artist = artist
        self.bpm = bpm
        self.genre = genre

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_bpm(self):
        return self.bpm

    def get_genre(self):
        return self.genre

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.bpm} bpm, {self.genre})'

    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.bpm}, {self.genre})"

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist
