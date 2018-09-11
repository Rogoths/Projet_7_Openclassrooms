from googlemaps import GoogleMaps

import urllib.request

from io import BytesIO
import json

def test_request_data(monkeypatch):
    result = [{
            'results': " "
            }
        ]

    def mockreturn(request):
        return BytesIO(json.dumps(result).encode())


    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    gmaps = GoogleMaps()
    assert gmaps.request_data() == result
