from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Seja bem vindo,  %s ' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/post2/<int:post_id>')
def show_post2(post_id):
    return 'Post %d' % post_id

@app.route('/barbearia/<path:endereco>')
def barbearia(endereco):
    return 'Rua Baubuena de Souza, 4 sala 19'

@app.route('/barbearia/<int:telefone>')
def contato(telefone):
    return 'Entre em contato e agende seu corte.'

if __name__ == '__main__':
    app.run(debug=True)
