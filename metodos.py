from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Processando o login..."
    else:
        return "Exibindo formulário de login..."

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        return "Exibindo formulário de login..."
    else:
        return "Exibindo outra página..."

if __name__ == '__main__':
    app.run(debug=True)
