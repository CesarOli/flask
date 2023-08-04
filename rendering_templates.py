from flask import Flask

app = Flask(__name__)
@app.route('/hello/<user>', method=['POST', 'GET'])
def hello(user):
    if request.methods == 'POST':