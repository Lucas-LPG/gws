from flask import Blueprint, request, render_template, redirect, url_for, session, redirect


actuator = Blueprint("actuator", __name__, template_folder="templates")
sensores = {'Umidade': 55, 'temperatura': 70, 'luminosidade': 20}


atuadores = {'Servo': 122, 'Interruptor': 1, 'Lampada Inteligente': 1}


# ATUADORES
@actuator.route('/register_actuator')
def register_actuators():
    if not session.get('user'):
        return redirect('/')
    global is_admin
    return render_template("register_actuator.html", user=session.get('user'))


@actuator.route('/add_actuator', methods=['GET', 'POST'])
def add_actuators():
    if not session.get('user'):
        return redirect('/')
    global atuadores
    if request.method == 'POST':
        atuador = request.form['name']
        condition = request.form['condition']
        atuadores[atuador] = condition
        return render_template("actuators.html", atuadores=atuadores, user=session.get('user'))
    else:
        atuador = request.args.get('name', None)
        condition = request.args.get('condition', None)
        atuadores[atuador] = condition
        return render_template("actuators.html", atuadores=atuadores, user=session.get('user'))


@actuator.route('/actuators')
def list_actuators():
    if not session.get('user'):
        return redirect('/')
    global atuadores
    atuadores = {key: int(value) for key, value in atuadores.items()}
    return render_template("actuators.html", atuadores=atuadores, user=session.get('user'))


@actuator.route('/remove_actuator')
def remove_actuator():
    if not session.get('user'):
        return redirect('/')
    global is_admin
    return render_template("remove_actuator.html", atuadores=atuadores, user=session.get('user'))


@actuator.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    if not session.get('user'):
        return redirect('/')
    global atuadores
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    atuadores.pop(actuator)
    return redirect("/actuators")
