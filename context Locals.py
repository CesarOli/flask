from flask import request
from flask import Flask

app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

with app.request_context(environ):
    assert request.method == 'POST'