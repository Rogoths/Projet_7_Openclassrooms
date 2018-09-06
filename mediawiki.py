import requests
import json


class Mediawiki:

    def __init__(self, lat, lng):
        self.url = "https://en.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gscoord="+str(lat)+"|"+str(lng)+"&format=json"


    def request_wiki(self):
        data = requests.get(self.url)
        result = data.json()
        pageid = result['query']['geosearch'][0]["pageid"]#dont forget[0] for the list
        return pageid

if __name__ == "__main__":
    wiki = Mediawiki(48.858222222222,2.2945)
    request = wiki.request_wiki()
    print(request)
