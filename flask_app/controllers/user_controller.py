from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User


@app.route('/login_page')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    print(request.form)

    if not User.validate_login(request.form):
        return redirect('/login_page')

    logged_in_user = User.find_one_by_email(request.form)

    if logged_in_user:
        session['uid'] = logged_in_user.id
        session['first_name'] = logged_in_user.first_name
        return redirect('/properties')

    return redirect('/properties')

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
    print(request.form)

    if not User.validate(request.form):
        return redirect('/register_page')

    session['uid'] = User.create(request.form)
    session['first_name'] = request.form["first_name"]

    return redirect('/')

@app.route('/sign_out')
def sign_out():
    session.clear()
    return redirect('/')