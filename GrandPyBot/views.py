from GrandPyBot import app
from flask import render_template, request

@app.route('/')
def index():
    variable = request.args.get('variable', 'defaut')
    variable = variable[0:1]
    return render_template('base.html', variable=variable)


@app.route('/bonjour')

def bonjour():
    variable = request.args.get('variable')
    return 'bonjour !!' + variable
