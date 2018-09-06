import requests
import json


class Mediawiki:

    def __init__(self, lat, lng):
        self.url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gscoord="+str(lat)+"|"+str(lng)+"&format=json"


    def request_wiki(self):
        data = requests.get(self.url)
        result = data.json()
        pageid = result['query']['geosearch'][0]["pageid"]#dont forget[0] for the list
        return pageid

    def get_info(self):
        pageid = self.request_wiki()
        parameters = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'pageids': pageid
}
        data = requests.get('https://fr.wikipedia.org/w/api.php',params=parameters)
        result = data.json()
        extract = result['query']['pages'][str(pageid)]['extract']
        return extract

if __name__ == "__main__":
    wiki = Mediawiki(48.858222222222,2.2945)
    request = wiki.request_wiki()
    info = wiki.get_info()
    print(request)
    print(info)
