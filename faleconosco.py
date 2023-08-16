from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/faleconosco/', methods= ['GET', 'POST'])
def contact_us():