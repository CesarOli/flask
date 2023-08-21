from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logado na sessao como %s' % escape(session['username'])
    return 'Você ainda não esta logado!!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        
if __name__ == '__main__':
    app.run(debug=True)