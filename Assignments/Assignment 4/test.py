#!/bin/python3

from song import Song
from vitals import Vitals
from workout import Workout

w = Workout("session_001", "2024-03-10")
w.add_song(Song("Eye of the Tiger", "Survivor", 109, "rock"))
w.add_vital(Vitals(80, (116, 75), 98.2, "2024-03-10 09:00"))
w.add_vital(Vitals(90, (122, 78), 97.8, "2024-03-10 09:15"))

print(w.get_average_heart_rate())

empty = Workout("session_empty", "2024-03-10")
print(empty.get_average_heart_rate())