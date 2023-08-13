from flask import Flask, request, render_template, url_for
from datetime import date

app = Flask(__name__)
@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == 'POST':
        return 'Testando método POST'
    else:
        return 'O Método não foi requisitado'
    
    
'''@app.route('/hello/<user>', methods=['POST', 'GET'])
def hello(user):
    if request.method == 'POST':
        return "Processando seu login, seus dados são: " + request.form['idade'] + request.form['sexo'] + request.form['bairro']
    else:
        idade = request.args['idade']
        sexo = request.args['sexo']
        bairro = request.args['bairro']

        return idade + ' ' + sexo + ' ' + bairro
        return render_template('hello.html',
                           data=date.today(), 
                           name=user,
                           caminho=url_for('static',filename='teste.txt'))'''
if __name__=='__main__':
    app.run(debug=True)
