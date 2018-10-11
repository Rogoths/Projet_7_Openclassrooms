#from GrandPyBot import app
from flask import Flask, render_template, request, jsonify
from parser import Parser
from googlemaps import GoogleMaps
from mediawiki import Mediawiki
from config import KEY
from messages import random_messages

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('base.html', key_googlemaps=KEY)

@app.route('/ajax', methods=['GET', 'POST',])
def user_query():
    response = {}
    text = request.args.get('query')#input in html file
    lower_text = text.lower()#lower the text
    parser = Parser(lower_text)
    normalize_text = parser.convert_ascii()
    response["text"] = normalize_text
    gmaps = GoogleMaps(normalize_text)
    long, lat, adress = gmaps.get_geocoding()
    response["long"] = long
    response["lat"] = lat
    response["adress"] = adress
    wiki = Mediawiki(lat, long)
    m = random_messages()
    try:
        response["extract"] = str(m)+wiki.get_info()
    except Exception as e:
        print(e)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)#developer mode no need to restart the server
