import paho.mqtt.client as mqtt
from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

from db.connection import db
from models import Kit, User

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
    from controllers import (
        max_people_capacity,
        max_temperature_capacity,
        people,
        temperature,
    )

    admin_query = User.select_from_users(User.role == "admin")
    admin_users = 0 if len(admin_query) <= 0 else len(admin_query)
    operator_query = User.select_from_users(User.role == "operador")
    operator_users = 0 if len(operator_query) <= 0 else len(operator_query)
    statistic_query = User.select_from_users(User.role == "estatistico")
    statistic_users = 0 if len(statistic_query) <= 0 else len(statistic_query)
    people = people if people <= max_people_capacity else max_people_capacity
    people = people if people >= 0 else 0

    kits = Kit.select_all_from_kits()
    return render_template(
        "home.html",
        admin_users=admin_users,
        operator_users=operator_users,
        statistic_users=statistic_users,
        kits=kits,
        people=people,
        max_people_capacity=max_people_capacity,
        temperature=temperature,
        max_temperature_capacity=max_temperature_capacity,
    )


@login.route("/register_user")
@login_required
def register_user():
    return render_template("users/register_user.html")


@login.route("/add_user", methods=["GET", "POST"])
@login_required
def add_users():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        role = request.form["role"]
        existing_users = User.select_all_from_users()
        existing_users_names = [user.name for user in existing_users]
        if user in existing_users_names:
            return render_template(
                "users/register_user.html",
                error_message="Erro! Esse nome de usuário já existe",
            )
        elif role != "admin" and role != "operador" and role != "estatistico":
            return render_template(
                "users/register_user.html",
                error_message="Erro! O role deve ser: admin, operador ou estatistico",
            )
        else:
            new_user = User(user, password, role)
            db.session.add(new_user)
            db.session.commit()
            return render_template(
                "users/users.html", users=User.select_all_from_users()
            )
    else:
        return redirect("/users")


@login.route("/users")
@login_required
def list_users():
    users = User.select_all_from_users()
    return render_template("users/users.html", users=users)


@login.route("/delete_user")
@login_required
def remove_user():
    user_id = request.args.get("user_id", None)
    User.delete_user_by_id(user_id)
    return redirect("/users")


@login.route("/edit_user")
@login_required
def edit_user():
    user_id = request.args.get("user_id", None)
    user = User.select_user_by_id(user_id)
    if user == None:
        return redirect("/users")
    else:
        return render_template("users/edit_user.html", user=user)


@login.route("/edit_given_user", methods=["GET"])
@login_required
def edit_given_user():
    user_id = request.args.get("user_id", None)
    user_name = request.args.get("name", None)
    user_password = request.args.get("password", None)
    user_role = request.args.get("role", None)

    User.update_given_user(user_id, user_name, user_password, user_role)

    return redirect("/users")


@login.route("/")
@login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
