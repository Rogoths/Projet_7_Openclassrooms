#from GrandPyBot import app
from flask import Flask, render_template, request
from parser import Parser
from googlemaps import GoogleMaps
from mediawiki import Mediawiki

app = Flask(__name__)

@app.route('/')
def index():
    variable = request.args.get('variable', 'defaut')
    variable = variable[0:1]
    return render_template('base.html', variable=variable)


@app.route('/', methods=['POST'])
def user_query():
    text = request.form['text']#input in html file
    lower_text = text.lower()#lower the text
    parser = Parser(lower_text)
    normalize_text = parser.convert_ascii()
    gmaps = GoogleMaps(normalize_text)
    long, lat = gmaps.get_geocoding()
    wiki = Mediawiki(lat,long)
    extract = wiki.get_info()


    return render_template('base.html', variable=extract)

if __name__ == '__main__':
    app.run(debug=True)#developer mode no need to restart the server
