# app.py
import time
from flask import Flask, render_template, request, jsonify, session
from login import login
from sensors import sensor, sensores
from actuators import actuator, atuadores
import paho.mqtt.client as mqtt
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
import flask_login


import json

app = Flask(__name__)
app.secret_key = "lucaspucas"

app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
# app.config['MQTT_BROKER_URL'] = '192.168.0.77'
app.config['MQTT_BROKER_PORT'] = 1883
# Set this item when you need to verify username and password
app.config['MQTT_USERNAME'] = ''
# Set this item when you need to verify username and password
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5000  # Set KeepAlive time in seconds
# If your broker supports TLS, set it True
app.config['MQTT_TLS_ENABLED'] = False

mqtt_client = Mqtt()
mqtt_client.init_app(app)

topic_subscribe = "cz/enviar"
people = 90
temperature = 0
max_capacity = 100


app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensor, url_prefix='/')
app.register_blueprint(actuator, url_prefix='/')


@app.route('/')
def index():
    return render_template("index.html", user=session.get('user'))

@app.route('/login')
def login():
    session.pop('user', False)
    return render_template("login.html")


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    global temperature, people
    js = json.loads(message.payload.decode())
    temperature = js["temperature"]
    if js["exitPeople"] == 0 and people > 0:
        people -= 1
    elif js["enterPeople"] == 0:
        people += 1


@app.route('/publish_message', methods=['GET', 'POST'])
def publish_message():
    request_data = request.get_json()
    publish_result = mqtt_client.publish(
        request_data['topic'], request_data['message'])
    return jsonify(publish_result)


@app.route('/real_time', methods=['GET', 'POST'])
def real_time():
    global temperature, people
    values = {"Temperatura": temperature,
              "Pessoas": people}
    return render_template("real_time.html", values=values, user=session.get('user'), max_capacity=max_capacity, people=people)


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Broker Connected successfully')
        mqtt_client.subscribe(topic_subscribe)  # subscribe topic
    else:
        print('Bad connection. Code:', rc)


@mqtt_client.on_disconnect()
def handle_disconnect(client, userdata, rc):
    print("Disconnected from broker")


@app.errorhandler(404)
def page_not_found(error):
    logged = False    
    if session.get('user'):
        logged = True
    return render_template("error.html", error_message="Parece que a página não existe! Tente novamente!",  logged=logged), 404

@app.errorhandler(405)
def page_not_found(error):
    return render_template("error.html", error_message="Você não fez login!"), 405

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True),
