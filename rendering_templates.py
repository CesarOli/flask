from flask import Flask, request

app = Flask(__name__)
@app.route('/hello/<user>', method=['POST', 'GET'])
def hello(user):
    if request.methods == 'POST':
        return "Processando seu login...Por favor, aguarde!!"
    else:
        idade = request.args['idade']
        sexo = request.args['sexo']
        bairro = request.args['bairro']

        return idade + ' ' + sexo + ' ' + bairro
        return render_template('hello.html',
                           data=date.today(), 
                           name=user,
                           caminho=url_for('static',filename='teste.txt'))
