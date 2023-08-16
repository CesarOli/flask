from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/faleconosco/', methods= ['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        return render_template('faleconosco.html')

    else:
        return request.form['sugestoes']
    