from flask import Blueprint, request, render_template, redirect, url_for, session

sensor = Blueprint("sensor", __name__, template_folder="templates")
sensores = {'Umidade': 55, 'temperatura': 70, 'luminosidade': 20}


@sensor.route('/register_sensors')
def register_sensors():
    if not session.get('user'):
        return redirect('/')
    return render_template("sensors/register_sensor.html", user=session.get('user'))


@sensor.route('/add_sensors', methods=['GET', 'POST'])
def add_sensors():
    if not session.get('user'):
        return redirect('/')
    global sensores
    if request.method == 'POST':
        sensor = request.form['name']
        condition = request.form['condition']
        sensores[sensor] = condition
        return render_template("sensors.html", sensores=sensores, user=session.get('user'))
    else:
        sensor = request.args.get('name', None)
        condition = request.args.get('condition', None)
        sensores[sensor] = condition
        return render_template("sensors.html", sensores=sensores, user=session.get('user'))


@sensor.route('/sensors')
def list_sensors():
    if not session.get('user'):
        return redirect('/')
    global sensores
    sensores = {key: int(value) for key, value in sensores.items()}
    return render_template("sensors.html", sensores=sensores, user=session.get('user'))


@sensor.route('/remove_sensor')
def remove_sensor():
    if not session.get('user'):
        return redirect('/')
    return render_template("remove_sensor.html", sensores=sensores, user=session.get('user'))


@sensor.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    if not session.get('user'):
        return redirect('/')
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores.pop(sensor)
    return redirect("/sensors")
