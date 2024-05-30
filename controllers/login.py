import paho.mqtt.client as mqtt
from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    current_user,
    logout_user,
)
from models import User, Kit

login = Blueprint("login", __name__, template_folder="templates")


@login.route("/login", methods=["GET", "POST"])
def login_func():
    if request.method == "POST":
        username = request.form["user"]
        password = request.form["password"]
        user = User.validate_user(username, password)

        if user:
            login_user(user)
            session["user"] = user.id
            return redirect(url_for("login.home"))
        else:
            return render_template(
                "login.html", login_message="Erro! Esse usuário não existe!"
            )

    return render_template("login.html")


@login.route("/home")
@login_required
def home():
    admin_query = User.select_from_users(User.role == "admin")
    admin_users = 0 if len(admin_query) <= 0 else len(admin_query)
    operator_query = User.select_from_users(User.role == "operador")
    operator_users = 0 if len(operator_query) <= 0 else len(operator_query)
    statistic_query = User.select_from_users(User.role == "estatistico")
    statistic_users = 0 if len(statistic_query) <= 0 else len(statistic_query)
    kits = Kit.select_all_from_kits()
    return render_template(
        "home.html",
        admin_users=admin_users,
        operator_users=operator_users,
        statistic_users=statistic_users,
        kits=kits,
    )


@login.route("/register_user")
@login_required
def register_user():
    return render_template("users/register_user.html", user=session.get("user"))


@login.route("/add_user", methods=["GET", "POST"])
@login_required
def add_users():
    global users
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        if user in users or user == "lucas":
            return render_template(
                "errors/error.html", error_message="Esse nome de usuário já existe!"
            )
        else:
            users[user] = password
            return render_template("users/users.html", users=users)


@login.route("/users")
@login_required
def list_users():
    users = User.select_all_information_from_users()
    return render_template("users/users.html", users=users, user=User.select_user_by_id(session.get('user')))


@login.route("/remove_user")
@login_required
def remove_user():
    users = User.select_all_information_from_users()
    return render_template("remove_user.html", users=users)


@login.route("/del_user", methods=["GET", "POST"])
@login_required
def del_user():
    if request.method == "POST":
        user = request.form["user"]
    else:
        user = request.args.get("user", None)
    User.delete_user_by_id(user)
    return redirect("/users")


@login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
