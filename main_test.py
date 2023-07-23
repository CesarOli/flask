from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Você está na página principal.'

@app.route('/login')
def login():
    return input('Digite seu login: ')