from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'A página do projeto'

@app.route('/sobre')
def sobre():
    return 'A página sobre'

