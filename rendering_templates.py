from flask import Flask,render_template, request, url_for
from time import sleep
from datetime import date

app = Flask(__name__)

@app.route('/hello/<user>', methods=['GET', 'POST'])
def hello(user):
    if request.method == 'POST':
        return "Processando o login..."
    else:
        return render_template('hello.html',
                               data=date.today(),                               
                               name=user,
                               caminho=url_for('static', filename='teste.txt'))

if __name__ == '__main__':
    app.run(debug=True)



