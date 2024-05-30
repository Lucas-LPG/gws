from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
    session,
    redirect,
)
from models.actuators import Actuator
from flask_login import login_required
from models.users import User


actuator = Blueprint("actuator", __name__, template_folder="templates")


@actuator.route("/register_actuator")
@login_required
def register_actuators():
    return render_template("actuators/register_actuator.html", user=session.get("user"))


# @sensor_.route('/edit_sensor')
# def edit_sensor():
#     id = request.args.get('id', None)
#     sensor = Sensor.get_single_sensor(id)
#     return render_template("update_sensor.html", sensor=sensor)


@actuator.route("/actuators")
@login_required
def list_actuators():
    local_user = User.select_user_by_id(session['user'])
    actuators = Actuator.select_all_from_actuator()
    return render_template("actuators/actuators.html", actuators=actuators, user=User.select_user_by_id(session.get('user')))


@actuator.route("/remove_actuator")
@login_required
def remove_actuator():
    actuators = Actuator.select_all_from_actuator()
    return render_template("remove_actuator.html",  actuators=actuators, user=session.get('user'))


@actuator.route("/add_actuator", methods=["GET", "POST"])
@login_required
def add_actuators():
    if request.method == 'POST':
        kit_name = request.form['kit_name']
        kit_id = request.form['kit_id']
        user_id = request.form['user_id']
        name = request.form['name']
        value = request.form['value']
        topic = request.form['topic']
        Actuator.insert_actuator(kit_name, kit_id, user_id, name, value, topic)
        actuators = Actuator.select_all_from_actuator()
        return render_template("actuators/actuators.html", actuators=actuators, user=session.get('user'))


@actuator.route("/update_actuator", methods=["GET", "POST"])
@login_required
def update_actuator():
    if request.method == 'POST':
        actuator_id = request.form.get("actuator_id")
        name = request.form.get("name")
        value = request.form.get("value")
        topic = request.form.get("topic")
        print(actuator_id, name, value, topic)
        Actuator.update_actuator_by_id(actuator_id, name, value, topic)
        actuators = Actuator.select_all_from_actuator()
        return render_template("actuators/actuators.html", actuators=actuators, user=session.get('user'))


@actuator.route("/del_actuator", methods=["GET", "POST"])
@login_required
def del_actuator():
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    Actuator.delete_actuator_by_id(actuator)
    return redirect("/actuators")
