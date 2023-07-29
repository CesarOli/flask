from flask import request, Flask, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        if f:
            f.save('/projetos2/flask/venv-flask/' + secure_filename(f.teste.txt))
            return 'Arquivo enviado com sucesso!!'
        else:
            return 'Nenhum arquivo enviado'
    return render_template('teste.txt')

if __name__ == '__main__':
    app.run(debug=True)


