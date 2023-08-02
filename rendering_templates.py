from flask import Flask,render_template, request, url_for
from time import sleep

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return "Processando o login..."
    else:
        return render_template('hello.html',name='Filano', caminho=url_for('static', filename='teste.txt'))

if __name__ == '__main__':
    app.run(debug=True)



