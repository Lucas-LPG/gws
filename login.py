# login.py
import paho.mqtt.client as mqtt
from flask import Blueprint, request, render_template, redirect, url_for, session
# from duts import duts

from flask_mqtt import Mqtt
from flask_socketio import SocketIO


login = Blueprint("login", __name__, template_folder="templates")

users = {
    "degar": "1234",
    "renan": "4321"
}

admin = {
    "lucas": "lucas"
}


@login.route('/register_user')
def register_user():
    return render_template("register_user.html", user=session.get('user'))


@login.route('/add_user', methods=['GET', 'POST'])
def add_users():
    global users
    if not session.get('user') == 'lucas':
        return redirect('/')
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user in users or user == 'lucas':
            return render_template("error.html", error_message="Esse nome de usuário já existe!")
        else:
            users[user] = password
            return render_template("users.html", users=users)


@login.route('/users')
def list_users():
    global users
    return render_template("users.html", users=users, user=session.get('user'))


@login.route('/home', methods=['GET', 'POST'])
def home():
    print(session.get('user'))
    if session.get('user'):
        return render_template("index.html", user=session.get('user'))
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if (user in users and users[user] == password) or (user in admin and admin[user] == password):
            session['user'] = user
            return render_template('index.html', user=session.get('user'))
        else:
            return render_template("error.html", error_message="Esse usuário não existe!")
    else:
        return redirect("/")

@login.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", users=users)


@login.route('/del_user', methods=['GET', 'POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return redirect("/users")

@login.route('/logout')
def logout():
    session.pop('user', False)
    return redirect('/')