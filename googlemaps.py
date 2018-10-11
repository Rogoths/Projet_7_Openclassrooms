import requests
import json
from config import KEY
from parser import Parser


class GoogleMaps:
    """query for Google Maps API by the program"""

    def __init__(self, query):
        self.url_base = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.key = str("&key="+KEY)
        self.query = query

    def request_data(self):
        parser = Parser(self.query)
        parsed = parser.formated_string()
        url = requests.get(self.url_base+parsed+self.key)
        #url = json.load(open("tour_eiffel.json"))
        data_raw = url.json()

        return data_raw

    def get_geocoding(self):
        data = self.request_data()
        data_results = data["results"]
        data_error = data["status"]

        if data_error == "OK":
            for coords in data_results:
                adress = str("l'adresse de ta demande est ")+ coords["formatted_address"]
                components = coords["geometry"]["location"]
                long = components["lng"]
                lat = components["lat"]

                return long, lat, adress

        elif data_error == "ZERO_RESULTS":
            long = 0
            lat = 0
            adress = "Désolé. Je ne trouve aucun résultat :("

            return long, lat, adress

        else:
            long = 0
            lat = 0
            adress = "Désolé. Il semble y avoir un problème d'allignement des planètes. Veuillez communiquer le message d'erreur suivant à mon créateur : "+str(data_error)

            return long, lat, adress

if __name__ == "__main__":
    query = "paris"
    gmaps = GoogleMaps(query)
    print(gmaps.request_data())
    lng, lat, adress = gmaps.get_geocoding()
    print(lng)
    print(lat)
    print(adress)
