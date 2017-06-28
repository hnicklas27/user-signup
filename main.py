from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True

def noentry(entry):
    if entry == '':
        return True
    else:
        return False

def validlength(length):
    if len(length) < 3 or len(length) > 20:
        return False
    else:
        return True  

def passmatch(password,verify):
    if password != verify:
        return False
    else:
        return True
                                             

@app.route("/", methods=['POST'])
def errors():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if noentry(username):
        username_error = 'Please enter text'
    else:
        if not validlength(username):
            username_error = 'Username must be greater than 3 and less than 20 characters'

    if noentry(password):
        password_error = 'Please enter text'
    else:
        if not validlength(password):
            password_error = 'Password must be greater than 3 and less than 20 characters'

    if noentry(verify):
        verify_error = 'Please enter text'
    else:
        if not passmatch(password,verify):
            verify_error = 'Password and Verifcation must match'


    if email != '':
        if '@' not in email or '.' not in email:
            email_error = 'Please enter a valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect ('/welcome?username=' + username)
    else:
        return render_template('signup_page.html',
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error)    

@app.route("/welcome", methods=['GET','POST'])
def welcome_page(): 
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

@app.route("/")
def index():
    return render_template('signup_page.html')

app.run()        
