#from GrandPyBot import app
from flask import Flask, render_template, request, jsonify
from parser import Parser
from googlemaps import GoogleMaps
from mediawiki import Mediawiki
from config import KEY

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
    try:
        long, lat, adress = gmaps.get_geocoding()
        response["long"] = long
        response["lat"] = lat
        response["adress"] = "l'adresse de ta demande est "+adress
        wiki = Mediawiki(lat, long)
        response["extract"] = wiki.get_info()

        return jsonify(response)
    except Exception as e:# -*- coding: utf-8 -*-
        print("Erreur lors de la saisie de la requète:")
        print(e)
        response["extract"] = ""
        response["adress"] = "Je suis navré... je n'ai pas compris ta demande. Tu peux réessayer si tu veux :)"
        return jsonify(response)
'''
@app.route('/s', methods=['GET'])
def ajax_request():
    response = {}
    text = request.args.get('query')
    lower_text = text.lower()#lower the text
    lower_text = answer.lower()
    parser = Parser(lower_text)
    normalize_text = parser.convert_ascii()
    response["text"]=normalize_text
    gmaps = GoogleMaps(normalize_text)
    long, lat = gmaps.get_geocoding()
    response["long"] = long
    response["lat"] = lat
    wiki = Mediawiki(lat, long)
    extract = wiki.get_info()
    #return render_template('base.html', variable=extract)
    return jsonify(response)
'''

if __name__ == '__main__':
    app.run(debug=True)#developer mode no need to restart the server
