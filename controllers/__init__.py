# app_controller.py
from flask import Flask, render_template, request, jsonify, session
from db.connection import db, instance
import json
from flask_mqtt import Mqtt
import paho.mqtt.client as mqtt
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_login import login_required,  LoginManager, logout_user
from models import User


topic_subscribe = "cz/enviar"
temperature = 0
max_capacity = 100
people = 60
people = people if people <= max_capacity else max_capacity


def create_app():
    app = Flask(__name__,
                template_folder="./templates/",
                static_folder="./static/",
                root_path="./")
    app.secret_key = "lucaspucas"

    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_KEEPALIVE'] = 5000
    app.config['MQTT_TLS_ENABLED'] = False

    mqtt_client = Mqtt()
    mqtt_client.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login.login_func'

    # app.config['TESTING'] = False
    # app.config['SECRET_KEY'] = 'generated-secrete-key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = instance
    # db.init_app(app)

    # app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    # app.config['MQTT_BROKER_PORT'] = 1883
    # app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    # app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    # app.config['MQTT_KEEPALIVE'] = 5000  # Set KeepAlive time in seconds
    # app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

    # mqtt_client= Mqtt()
    # mqtt_client.init_app(app)

    topic_subscribe = "/aula_flask/"

    # @mqtt_client.on_connect()
    # def handle_connect(client, userdata, flags, rc):
    #     if rc == 0:
    #         print('Broker Connected successfully')
    #         mqtt_client.subscribe(topic_subscribe) # subscribe topic
    #     else:
    #         print('Bad connection. Code:', rc)

    # @mqtt_client.on_disconnect()
    # def handle_disconnect(client, userdata, rc):
    #     print("Disconnected from broker")

    # @mqtt_client.on_message()
    # def handle_mqtt_message(client, userdata, message):
    #     if(message.topic==topic_subscribe):
    #         global temperature, huminity
    #         print(message.payload.decode())

    @app.route('/')
    def index():
        return render_template("landing.html", user=session.get('user'))

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
            mqtt_client.subscribe(topic_subscribe)
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
        return render_template("errors/error.html", error_message="Parece que a página não existe! Tente novamente!",  logged=logged), 404

    @app.errorhandler(405)
    def page_not_found(error):
        return render_template("errors/error.html", error_message="Você não fez login!"), 405

    @login_manager.request_loader
    def load_user_from_request(request):

        # first, try to login using the api_key url arg
        api_key = request.args.get('api_key')
        if api_key:
            user = User.query.filter_by(api_key=api_key).first()
            if user:
                return user

        # next, try to login using Basic Auth
        api_key = request.headers.get('Authorization')
        if api_key:
            api_key = api_key.replace('Basic ', '', 1)
            try:
                api_key = base64.b64decode(api_key)
            except TypeError:
                pass
            user = User.query.filter_by(api_key=api_key).first()
            if user:
                return user

        # finally, return None if both methods did not login the user
        return None

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
