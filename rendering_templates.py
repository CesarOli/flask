from flask import Flask,render_template, request
from time import sleep

#Falar com Fernando, criei o arquivo .html na pasta raiz Templates.
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return "Processando o login..."
    else:
        return render_template("hello.html")

if __name__ == '__main__':
    app.run(debug=True)
