from flask import Flask, request

app = Flask(__name__)
@app.route('/hello/<user>', method=['POST', 'GET'])
def hello(user):
    if request.methods == 'POST':
        return "Processando seu login...Por favor, aguarde!!"
