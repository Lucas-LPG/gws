from flask import Blueprint, request, render_template, redirect, session
from models import User
from flask_login import login_required
from models.sensors import Sensor

sensor = Blueprint("sensor", __name__, template_folder="templates")


@sensor.route("/register_sensors")
@login_required
def register_sensors():
    return render_template("sensors/register_sensor.html", user=User.select_user_by_id(session.get("user")))


@sensor.route("/sensors")
@login_required
def list_sensors():
    sensors = Sensor.select_all_from_sensor()
    return render_template("sensors/sensors.html", sensors=sensors, user=User.select_user_by_id(session.get('user')))


@sensor.route("/add_sensors", methods=["GET", "POST"])
@login_required
def add_sensors():
    if request.method == 'POST':
        kit_name = request.form['kit_name']
        kit_id = request.form['kit_id']
        user_id = request.form['user_id']
        name = request.form['name']
        value = request.form['value']
        topic = request.form['topic']
        Sensor.insert_sensor(kit_name, kit_id, user_id, name, value, topic)
        sensors = Sensor.select_all_from_sensor()
        return render_template("sensors/sensors.html", sensors=sensors, user=User.select_user_by_id(session.get('user')))


@sensor.route("/update_sensor", methods=["GET", "POST"])
@login_required
def update_sensor():
    if request.method == 'POST':
        sensor_id = request.form.get("sensor_id")
        name = request.form.get("name")
        value = request.form.get("value")
        topic = request.form.get("topic")
        Sensor.update_sensor_by_id(sensor_id, name, value, topic)
        sensors = Sensor.select_all_from_sensor()
        return render_template("sensors/sensors.html", sensors=sensors, user=User.select_user_by_id(session.get('user')))


@sensor.route("/remove_sensor")
@login_required
def remove_sensor():
    sensors = Sensor.select_all_from_sensor()
    return render_template("remove_sensor.html", sensors=sensors, user=User.select_user_by_id(session.get('user')))


@sensor.route("/del_sensor", methods=["GET", "POST"])
@login_required
def del_sensor():
    if request.method == "POST":
        sensor = request.form["sensor"]
    else:
        sensor = request.args.get("sensor", None)
    Sensor.delete_sensor_by_id(sensor)
    return redirect("/sensors")
