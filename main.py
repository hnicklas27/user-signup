from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def noentry():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']

    if username == '':
        error = ""


@app.route("/")
def index():
    return render_template('signup_page.html',
        )

app.run()        
