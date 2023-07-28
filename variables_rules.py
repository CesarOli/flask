from flask import Flask
app = Flask(__name__)

@app.route('/user/<Cesar>')
def show_user_profile(Cesar):
    return 'Seja bem vindo,  %s ' % Cesar

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % 8

@app.route('/post2/<int:post_id>')
def show_post2(post_id):
    return 'Post %d' % 13

if __name__ == '__main__':
    app.run(debug=True)
