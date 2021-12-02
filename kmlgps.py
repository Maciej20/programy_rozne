#Program "wyciąga" koordynaty GPS ze wszystkich zdjęć w folderze, zamienia nazwy zdjęć na wygodniejsze
#i z koordynatów tworzy warstwę KML

from GPSPhoto import gpsphoto
import os
import simplekml


directory = os.path.realpath(__file__).rstrip("\kmlgps.py") ## ścieżka dostępu do pliku
counter = 99
a = 0
b = 0
kml=simplekml.Kml()

prefix = input("wprowadz prefix: ")

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        counter += 1
        a = gpsphoto.getGPSData(filename)["Latitude"]
        b = gpsphoto.getGPSData(filename)["Longitude"]
        os.rename(filename, f"{prefix}{counter}.jpg")
        kml.newpoint(name=f"{prefix}{counter}", coords = [(b,a)])
        
kml.save(f'{prefix}100-{prefix}{counter}.kml')