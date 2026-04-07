from clinic import Clinic

c = Clinic("FitTrack Clinic")
c.load_csv("patients.csv")

averages = c.get_genre_hr_averages()
for genre, avg in sorted(averages.items()):
    print(genre + ": " + str(round(avg, 1)) + " bpm")