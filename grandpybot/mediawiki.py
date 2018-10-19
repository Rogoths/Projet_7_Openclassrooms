import requests
import json


class Mediawiki:

    def __init__(self, lat, lng):
        self.url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=10000&gscoord="+str(lat)+"|"+str(lng)+"&format=json"

    def request_wiki(self):
        """with long lat get the pageid of the user request"""
        try:
            data = requests.get(self.url)
            result = data.json()
            pageid = result['query']['geosearch'][0]["pageid"]#dont forget[0] for the list
            print(type(data))
            return pageid
        except Exception as e:
            print(e)
            pass

    def get_info(self):
        """request an extract with the pageid"""
        pageid = self.request_wiki()
        parameters = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
            'pageids': pageid
            }
        try:
            data = requests.get('https://fr.wikipedia.org/w/api.php',params=parameters)
            result = data.json()
            extract = result['query']['pages'][str(pageid)]['extract']
            return extract

        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    wiki = Mediawiki(48.858222222222,2.2945)
    request = wiki.request_wiki()
    info = wiki.get_info()
    print(request)
    print(info)
