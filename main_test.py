from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Você está na página principal.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    #tentei retornar o conteúdo do arquivo .txt
    return url_for('static', filename='teste.txt')

'''@app.route('/login', methods=['GET', 'POST'])
def login():
    with open('static/teste.txt', 'r') as file:
        content = file.read()
    return content
'''

@app.route('/profile/<profilename>')
def profile(profilename):
    print (url_for('login', next = '/'))
    return profilename

# revisar com o Fernando esta parte
with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login', next = '/'))
    print (url_for('profile', profilename = 'César' ))


if __name__ == '__main__':
    app.run(debug=True)