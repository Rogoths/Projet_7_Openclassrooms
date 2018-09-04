import requests
from config import KEY
from parser import Parser


class GoogleMaps:
    """query for Google Maps API by the program"""

    def __init__(self):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address"
        self.query = "=&"
        self.key = str("key="+KEY)

    def get_geocoding(self):
        parser = Parser("peux-tu me donner l'adresse d'openclassrooms à paris")
        parsed = parser.formated_string()
        url = self.url+self.query+parsed+self.key
        return url

if __name__ == "__main__":

    gmaps = GoogleMaps()
    print(gmaps.get_geocoding())
