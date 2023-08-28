from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/faleconosco/', methods= ['GET', 'POST'])
def contact_us():
        return render_template('faleconosco.html')


if __name__=='__main__':
    app.run(debug=True)

#criar label
#garantir o preenchimentos de ambos os campos do formulário.
#garantir que a rota aceite a requisição somente com o preenchimento dos dois campos 
#campos sugestões e email
#retornar mensagem de sucesso para o usuário, + email cadastrado.
# não dispensar os dados enviados 'email' e 'sugestões'
# colocar 'Fale Conosco' 