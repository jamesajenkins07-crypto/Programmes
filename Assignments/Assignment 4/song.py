# Name: James Jenkins
# Student #: 251491498
# Username: jjenki4
# Date: 30/03/2026
# Description: Defines the Song class, which represents a single music
#              track in a workout session playlist.

class Song:

    # Description: Initialises a new Song instance with the given values.
    # Parameters: title (string), artist (string), bpm (int), genre (string)
    # Returns: None
    def __init__(self, title, artist, bpm, genre):
        self._title = title
        self._artist = artist
        self._bpm = bpm
        self._genre = genre

    # Description: Returns the title of the song.
    # Parameters: None
    # Returns: title (string)
    def get_title(self):
        return self._title

    # Description: Returns the artist of the song.
    # Parameters: None
    # Returns: artist (string)
    def get_artist(self):
        return self._artist

    # Description: Returns the bpm of the song.
    # Parameters: None
    # Returns: bpm (int)
    def get_bpm(self):
        return self._bpm

    # Description: Returns the genre of the song.
    # Parameters: None
    # Returns: genre (string)
    def get_genre(self):
        return self._genre

    # Description: Returns a string representation of the song.
    # Parameters: None
    # Returns: string in format '"<title>" by <artist> (<bpm> bpm, <genre>)'
    def __str__(self):
        return f'"{self._title}" by {self._artist} ({self._bpm} bpm, {self._genre})'

    # Description: Returns a string representation of the song for debugging.
    # Parameters: None
    # Returns: string in format 'Song('<title>', '<artist>', <bpm>, '<genre>')'
    def __repr__(self):
        return f"Song('{self._title}', '{self._artist}', {self._bpm}, '{self._genre}')"

    # Description: Two Song instances are equal if they have the same title and artist.
    # Parameters: other (Song)
    # Returns: True if self and other have the same title and artist, False otherwise.
    def __eq__(self, other):
        return self._title == other._title and self._artist == other._artist
