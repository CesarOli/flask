from flask import Flask, url_for
app = Flask(__name__)

@app.route ( '/login' ,  methods = [ 'GET' ,  'POST' ]) 
def  login (): 
    if  request . methods  ==  'POST' : 
        do_the_login () 
    else : 
        show_the_login_form ()

if __name__ == '__main__':
    app.run(debug=True)