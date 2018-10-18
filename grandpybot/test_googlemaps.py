from .googlemaps import GoogleMaps

import requests

import json

class Request_mock:
    """mocking a gmaps requests"""

    def __init__(self, result):

        self.result = result

    def json(self):

        return json.dumps(self.result)

def test_request_data(monkeypatch):
    result = [{
            "results": " "
            }
        ]

    def mockreturn(request):

        response = Request_mock(result)

        return response

    monkeypatch.setattr(requests,"get", mockreturn)
    gmaps = GoogleMaps("compiegne")
    assert json.loads(gmaps.request_data()) == result
