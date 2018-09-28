from mediawiki import Mediawiki

import urllib.request
import json


def test_request_wiki(monkeypatch):
    results = {"query":
                {"geosearch"
                [{
                    "pageid": "4641538",
                    }
                    ]
                }
            }

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    m = Mediawiki(5,5)
    assert m.request_wiki() == results
