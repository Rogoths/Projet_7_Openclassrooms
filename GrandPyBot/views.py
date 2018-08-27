from GrandPyBot import app
from flask import render_template, request
from parser import Parser

@app.route('/')
def index():
    variable = request.args.get('variable', 'defaut')
    variable = variable[0:1]
    return render_template('base.html', variable=variable)


@app.route('/bonjour')

def bonjour():
    variable = request.args.get('variable')
    parser = Parser(variable)
    parsed_input = parser.string_convert()
    return 'bonjour !!' + parsed_input
