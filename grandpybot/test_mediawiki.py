from .mediawiki import Mediawiki

import json

import requests

class Request_mock:

    def __init__(self, result):

        self.result = result

    def json(self):

        return self.result

def test_request_data(monkeypatch):
    result = {'batchcomplete': '', 'query': {'geosearch': [{'pageid': 4641538, 'ns': 0, 'title': 'Le Jules Verne', 'lat': 48.85825, 'lon': 2.2945, 'dist': 3.1, 'primary': ''}, {'pageid': 1869201, 'ns': 0, 'title': 'Exposition universelle de Paris de 1889', 'lat': 48.8583, 'lon': 2.29417, 'dist': 25.6, 'primary': ''}, {'pageid': 5828872, 'ns': 0, 'title': 'Buste de Gustave Eiffel par Antoine Bourdelle', 'lat': 48.858694, 'lon': 2.2944, 'dist': 53, 'primary': ''}, {'pageid': 1359783, 'ns': 0, 'title': 'Tour Eiffel', 'lat': 48.858, 'lon': 2.2953, 'dist': 63.5, 'primary': ''}, {'pageid': 5422123, 'ns': 0, 'title': 'Avenue Gustave-Eiffel', 'lat': 48.857388, 'lon': 2.29463, 'dist': 93.2, 'primary': ''}, {'pageid': 2689115, 'ns': 0, 'title': 'Rives de la Seine à Paris', 'lat': 48.85889, 'lon': 2.29333, 'dist': 113.3, 'primary': ''}, {'pageid': 4424460, 'ns': 0, 'title': 'Allée des Refuzniks', 'lat': 48.857388, 'lon': 2.293028, 'dist': 142.1, 'primary': ''}, {'pageid': 7488373, 'ns': 0, 'title': "Grande lunette de l'exposition universelle de Paris 1900", 'lat': 48.8575, 'lon': 2.29289, 'dist': 142.6, 'primary': ''}, {'pageid': 5422017, 'ns': 0, 'title': 'Allée Jean-Paulhan', 'lat': 48.859347, 'lon': 2.295585, 'dist': 148.1, 'primary': ''}, {'pageid': 5422020, 'ns': 0, 'title': 'Allée Léon-Bourgeois', 'lat': 48.857236, 'lon': 2.292704, 'dist': 171.1, 'primary': ''}]}}

    def mockreturn(request):

        response = Request_mock(result)

        return response

    monkeypatch.setattr(requests,"get", mockreturn)
    wiki = Mediawiki(5,5)
    test = wiki.request_wiki()
    assert wiki.request_wiki() == result["query"]["geosearch"][0]["pageid"]
