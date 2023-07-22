from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/teste')
def teste():
    return 'Testando Flask'

@app.route('/user/<Cesar>')
def show_user_profile(Cesar):
    return 'Seja bem vindo,  %s ' % Cesar

if __name__ == '__main__':
    app.run(debug=True)

