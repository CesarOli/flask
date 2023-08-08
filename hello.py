from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
def hello():
    return 'Hello World!'

@app.route('/teste/')
def teste():
    return 'Testando Flask'

@app.route('/projects')
def projects():
    return 'A página do projeto'

@app.route('/sobre/')
def sobre():
    return 'A página sobre'

@app.route('/barbearia/')
def home():
    return 'Entre em contato conosco.'
if __name__ == '__main__':
    app.run(debug=True)

