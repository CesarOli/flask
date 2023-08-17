from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/faleconosco/', methods= ['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        return render_template('faleconosco.html')

    elif request.method == 'GET':
        return request.form['sugestoes']
    

if __name__=='__main__':
    app.run(debug=True)