from flask import Blueprint, request, render_template, redirect, url_for, session, redirect
# from db.operations import select_db
from models.actuators import Actuator


actuator = Blueprint("actuator", __name__, template_folder="templates")
sensores = {'Umidade': 55, 'temperatura': 70, 'luminosidade': 20}

actuators = {'Servo': 122, 'Interruptor': 1, 'Lampada Inteligente': 1}
# actuators = select_db(Actuator, '')


@actuator.route('/register_actuator')
def register_actuators():
    if not session.get('user'):
        return redirect('/')
    return render_template("actuators/register_actuator.html", user=session.get('user'))


@actuator.route('/add_actuator', methods=['POST'])
def add_actuators():
    if not session.get('user'):
        return redirect('/')
    global actuators
    if request.method == 'POST':
        kit_name = request.form['kit_name']
        user_id = request.form['user_id']
        name = request.form['name']
        value = request.form['value']
        topic = request.form['topic']
        Actuator.insert_actuator(kit_name, user_id, name, value, topic)
        return render_template("actuators/actuators.html", actuators=actuators, user=session.get('user'))
    else:
        atuador = request.args.get('name', None)
        condition = request.args.get('condition', None)
        actuators[atuador] = condition
        return render_template("actuators/actuators.html", actuators=actuators, user=session.get('user'))


@actuator.route('/actuators')
def list_actuators():
    if not session.get('user'):
        return redirect('/')
    global actuators
    actuators = {key: int(value) for key, value in actuators.items()}
    return render_template("actuators/actuators.html", actuators=actuators, user=session.get('user'))


@actuator.route('/remove_actuator')
def remove_actuator():
    if not session.get('user'):
        return redirect('/')
    return render_template("remove_actuator.html", actuators=actuators, user=session.get('user'))


@actuator.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    if not session.get('user'):
        return redirect('/')
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.pop(actuator)
    return redirect("/actuators")
