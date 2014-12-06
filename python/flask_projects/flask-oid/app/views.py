from app import app, oid
from flask import Flask, request, render_template, redirect, g, session, url_for
from config import OPENID_PROVIDERS
from forms import LoginForm

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print form.oid_provider.data
        oid_url = OPENID_PROVIDERS[form.oid_provider.data]
        return oid.try_login(oid_url, 
            ask_for = ['nickname', 'email'])
        
    return render_template('login.html', 
        title = 'Sign In',
        form = form)



""" From https://developers.google.com/google-apps/marketplace/best_practices

##Claimed identifiers vs. email addresses

Additionally, email service providers may close a user's email account or 
recycle the username. Basically, the johndoe@example.com you knew 2 years ago 
might not be the same johndoe@example.com today, which is why using synthetic 
identifiers is so important to security.

"""
@oid.after_login
def after_login(resp):
    print "in after_login"
    return render_template("oid-response.html", 
        email = resp.email,
        identity_url = resp.identity_url)
