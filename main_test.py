from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Você está na página principal.'

@app.route('/nome')
def login():
    return input('Digite seu nome: ')

@app.route('/user/<Cesar>')
def profile(Cesar):
    return input('Digite seu username: ')

