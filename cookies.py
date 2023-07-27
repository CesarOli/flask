from flask import Flask, request, render_template
app = Flask(__name__)

'''@app.route('/')
def index():
    username = request.cookies.get('username')'''


@app.route('/')
def index():
    resp = make_response(render_template())
    resp.set_cookie('username', 'the username')
    return resp

if __name__ == '__main__':
    app.run(debug=True)