from flask import Blueprint, request, render_template, redirect, url_for, session
from models import User
from models.sensors import Sensor

sensor = Blueprint("sensor", __name__, template_folder="templates")


@sensor.route('/register_sensors')
def register_sensors():
    if not session.get('user'):
        return redirect('/')
    return render_template("sensors/register_sensor.html", user=session.get('user'))


@sensor.route('/add_sensors', methods=['GET', 'POST'])
def add_sensors():
    if not session.get('user'):
        return redirect('/')
    if request.method == 'POST':
        kit_name = request.form['kit_name']
        user_id = request.form['user_id']
        name = request.form['name']
        value = request.form['value']
        topic = request.form['topic']
        Sensor.insert_sensor(kit_name, user_id, name, value, topic)
        sensors = Sensor.select_all_from_sensor()
        return render_template("sensors/sensors.html", sensors=sensors, user=session.get('user'))


@sensor.route('/sensors')
def list_sensors():
    sensors = Sensor.select_all_from_sensor()
    print(sensors)
    return render_template("sensors/sensors.html", sensors=sensors, user=session.get('user'))


@sensor.route('/remove_sensor')
def remove_sensor():
    if not session.get('user'):
        return redirect('/')
    sensors = Sensor.select_all_from_sensor()
    return render_template("remove_sensor.html", sensors=sensors, user=session.get('user'))


@sensor.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    if not session.get('user'):
        return redirect('/')
    # global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    # sensores.pop(sensor)
    return redirect("/sensors")
