from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')