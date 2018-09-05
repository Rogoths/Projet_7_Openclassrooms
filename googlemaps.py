import requests
import json
from config import KEY
from parser import Parser


class GoogleMaps:
    """query for Google Maps API by the program"""

    def __init__(self):
        self.url_base = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.key = str("key="+KEY)

    def request_data(self):
        parser = Parser(" d'openclassrooms à paris")
        parsed = parser.formated_string()
        #url = requests.get(self.url_base+parsed+self.key)
        url = json.load(open("tour_eiffel.json"))
        #data_raw = url.json()
        return url


    def get_geocoding(self):
        data = self.request_data()
        data_results = data["results"]

        for coords in data_results:
            components = coords["geometry"]["location"]
            long = components["lng"]
            lat = components["lat"]
            geocode = long,lat

            return geocode

        #return data




if __name__ == "__main__":

    gmaps = GoogleMaps()
    #print(gmaps.request_data())
    print(gmaps.get_geocoding())
