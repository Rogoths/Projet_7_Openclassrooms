import requests
from config import KEY


class GoogleMaps:
    """query for Google Maps API by the program"""

    def __init__(self):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?"
        self.query = "address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key="
        self.key = str(KEY)
