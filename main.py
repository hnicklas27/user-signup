from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def noentry():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    error = "Please enter text"

    if username == '':
        return error
    if password == '':
        return error
    if verify_password == '':
        return error  

@app.route("/", methods=['POST'])    
def notvalid():
    username_length = request.form['username']
    password_length = request.form['password']
    error = "Entry must be longer than 3 character and less than 20."

    if len(username_length) < 3 or len(username_length) > 20:
        return error
    if len(password_length) < 3 or len(username_length) > 20:  
        return error

@app.route("/", methods=['POST'])
def passmatch():
    password = request.form['password']
    verify_password= request.form['verify']
    error = "Password and Verification must match"

    if password != verify_password:
        return error

@app.route("/",methods=['POST'])
def emailerror():
    email = request.form['email']
    error = "Please enter a valid email"

    if email == '':
        pass
    elif '@' not in email and '.' not in email:
        return error
    elif email < 3 or email > 20:
        return error        

@app.route("/welcome", methods=['GET','POST'])
def welcome_page():
    return render_template('welcome.html',
        username = username)

@app.route("/")
def index():
    return render_template('signup_page.html',
        )

app.run()        
