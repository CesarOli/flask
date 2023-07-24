from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Você está na página principal.'

@app.route('/login')
def login():
    return input('Digite seu login: ')

@app.route('/profile/<profile>')
def profile():
    return input('Digite seu profile: ')

# revisar com o Fernando esta parte
with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login', next = '/'))
    print (url_for('profile', profile = 'John Doe' ))


if __name__ == '__main__':
    app.run(debug=True)