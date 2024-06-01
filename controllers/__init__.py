# app_controller.py
import json

import paho.mqtt.client as mqtt
from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_login import LoginManager, login_required, logout_user
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

from db.connection import db, instance
from models import Actuator, Device, Historic, Kit, Sensor, User

topic_recive = "cz/enviar"
topic_send = "cz/receba"
temperature = 0
max_people_capacity = 100
max_temperature_capacity = 50
people = 0
last_update_dht = 0
last_update_people = 0
ar_condicionado = 0


def create_app():
    app = Flask(
        __name__,
        template_folder="./templates/",
        static_folder="./static/",
        root_path="./",
    )
    app.secret_key = "lucaspucas"

    app.config["MQTT_BROKER_URL"] = "mqtt-dashboard.com"
    app.config["MQTT_BROKER_PORT"] = 1883
    app.config["MQTT_USERNAME"] = ""
    app.config["MQTT_PASSWORD"] = ""
    app.config["MQTT_KEEPALIVE"] = 5000
    app.config["MQTT_TLS_ENABLED"] = False

    mqtt_client = Mqtt()
    mqtt_client.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login.login_func"

    @app.route("/")
    def index():
        return render_template("landing.html", user=session.get("user"))

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        global topic_recive
        if message.topic == topic_recive:
            try:
                js = json.loads(message.payload.decode())
                global people, temperature, last_update_people, last_update_dht
                with app.app_context():
                    dht = Sensor.select_device_by_sensor_id(1)
                    Sensor.update_sensor_value(dht.id, js["temperature"])
                    temperature = dht.value

                    last_update_dht = Historic.select_datetime_by_device_id(dht.id)
                if js["exitPeople"] == 0:
                    with app.app_context():
                        actuator = Actuator.select_actuators_by_id(2)
                        Actuator.update_actuator_button_value(actuator.device_id, 1)
                        last_update_people = Historic.select_datetime_by_device_id(
                            actuator.device_id
                        )
                elif js["enterPeople"] == 0:
                    with app.app_context():
                        actuator = Actuator.select_actuators_by_id(1)
                        Actuator.update_actuator_button_value(actuator.device_id, 1)
                        last_update_people = Historic.select_datetime_by_device_id(
                            actuator.device_id
                        )
                with app.app_context():
                    people = (
                        Actuator.select_device_by_actuator_id(1).value
                        - Actuator.select_device_by_actuator_id(2).value
                    )
            except:
                print("erro")

    @app.route("/kits")
    @login_required
    def kits():

        kits = Kit.select_all_from_kits()
        return render_template("kits/kits.html", kits=kits)

    @app.route("/edit_kit")
    @login_required
    def edit_kit():
        kit_id = request.args.get("kit_id", None)
        kit = Kit.select_kit_by_id(kit_id)
        user_name = User.select_user_by_id(kit.user_id).name
        error_message = request.args.get("error_message", None)
        if kit == None:
            return redirect("/kits")
        else:
            return render_template(
                "kits/edit_kits.html",
                kit=kit,
                user_name=user_name,
                error_message=error_message,
            )

    @app.route("/data_history", methods=["GET", "POST"])
    @login_required
    def data_history():
        if request.method == "POST":
            datetime_begin = request.form["datetime_begin"]
            datetime_end = request.form["datetime_end"]

            historics_sensors = Historic.select_by_datetime_from_Sensor_historic(
                datetime_begin, datetime_end
            )

            historic_actuators = Historic.select_by_datetime_from_Actuator_historic(
                datetime_begin, datetime_end
            )
            return render_template(
                "historic/data_history.html",
                historics_sensors=historics_sensors,
                historic_actuators=historic_actuators,
            )

        else:
            historics_sensors = Historic.select_all_from_sensor_historic()
            historic_actuators = Historic.select_all_from_actuator_historic()
            return render_template(
                "historic/data_history.html",
                historics_sensors=historics_sensors,
                historic_actuators=historic_actuators,
            )

    @app.route("/edit_given_kit")
    @login_required
    def edit_given_kit():
        kit_id = request.args.get("kit_id", None)
        kit_name = request.args.get("kit_name", None)
        user_name = request.args.get("user_name", None)
        existing_kit = Kit.select_kit_by_name(kit_name)
        kit = Kit.select_kit_by_id(kit_id).name
        existing_user = User.select_user_by_name(user_name)
        if existing_kit and kit_name != kit:
            return redirect(
                url_for(
                    ".edit_kit",
                    error_message="Esse nome de kit já existe!",
                    kit_id=kit_id,
                )
            )
        elif not existing_user:
            return redirect(
                url_for(
                    ".edit_kit",
                    error_message="Esse nome de usuário não existe!",
                    kit_id=kit_id,
                )
            )
        else:
            user_id = User.select_user_by_name(user_name).id
            Kit.update_given_kit(kit_id, kit_name, user_id)
            return redirect("/kits")

    @app.route("/delete_kit")
    @login_required
    def remove_kit():
        kit_id = request.args.get("kit_id", None)
        Kit.delete_kit_by_id(kit_id)
        return redirect("/kits")

    @app.route("/register_kit")
    @login_required
    def register_kit():
        error_message = request.args.get("error_message", None)
        return render_template("kits/register_kit.html", error_message=error_message)

    @app.route("/add_kit", methods=["GET", "POST"])
    @login_required
    def add_kit():
        if request.method == "POST":
            kit_name = request.form["kit"]
            user_name = request.form["user_name"]
            existing_kit = Kit.select_kit_by_name(kit_name)
            existing_user = User.select_user_by_name(user_name)
            if existing_kit:
                return redirect(
                    url_for(
                        ".register_kit", error_message="Esse nome de Kit já existe!"
                    )
                )
            elif not existing_user:
                return redirect(
                    url_for(".register_kit", error_message="Esse usuário não existe!")
                )
            else:
                new_kit = Kit(kit_name, existing_user.id)
                db.session.add(new_kit)
                db.session.commit()
                return redirect("/kits")

    @app.route("/devices")
    @login_required
    def devices():
        sensors = Sensor.select_all_from_sensors()
        actuators = Actuator.select_all_from_actuators()
        return render_template(
            "devices/devices.html", sensors=sensors, actuators=actuators
        )

    @app.route("/edit_device")
    @login_required
    def edit_device():
        device_type = request.args.get("device_type")
        device_id = request.args.get("device_id")
        error_message = request.args.get("error_message")

        print(device_type)
        if device_type == "actuator":
            actuator = Actuator.select_actuators_by_id(device_id)
            return render_template(
                "devices/edit_device.html",
                device=actuator,
                device_type=device_type,
                error_message=error_message,
            )
        elif device_type == "sensor":
            sensor = Sensor.select_sensors_by_id(device_id)
            return render_template(
                "devices/edit_device.html",
                device=sensor,
                device_type=device_type,
                error_message=error_message,
            )
        else:
            return render_template("devices/edit_device.html")

    @app.route("/edit_given_device")
    @login_required
    def edit_given_device():
        given_device_id = request.args.get("given_device_id", None)
        device_name = request.args.get("device_name", None)
        device_value = request.args.get("device_value", None)
        device_topic = request.args.get("device_topic", None)
        kit_name = request.args.get("kit_name", None)
        device_type = request.args.get("device_type", None)

        existing_device = Device.select_device_by_name(device_name)
        existing_kit = Kit.select_kit_by_name(kit_name)
        if existing_device:
            device_id = Device.select_device_by_name(device_name).id
        else:
            device_id = request.args.get("device_id")

        # Caso nome não seja alterado
        if not existing_device:
            return redirect(
                url_for(
                    ".edit_device",
                    error_message="Esse nome de dispositivo não existe!",
                    device_type=device_type,
                    device_id=device_id,
                )
            )
        elif not existing_kit:
            return redirect(
                url_for(
                    ".edit_device",
                    error_message="Esse kit não existe!",
                    device_type=device_type,
                    device_id=device_id,
                )
            )
        else:
            print(device_type)
            if device_type == "actuator":
                Actuator.update_given_actuator(
                    given_device_id,
                    device_id,
                    device_name,
                    device_value,
                    device_topic,
                    kit_name,
                )
            elif device_type == "sensor":
                Sensor.update_given_sensor(
                    given_device_id,
                    device_id,
                    device_name,
                    device_value,
                    device_topic,
                    kit_name,
                )
            print(device_type)
            return redirect("/devices")

    @app.route("/delete_device")
    @login_required
    def delete_device():
        device_type = request.args.get("device_type")
        device_id = request.args.get("device_id")
        print(device_id)

        if device_type == "sensor":
            sensor = Sensor.select_single_sensor_by_id(device_id)
            db.session.delete(sensor)
            db.session.commit()
        elif device_type == "actuator":
            actuator = Actuator.select_single_actuator_by_id(device_id)
            print(actuator)
            db.session.delete(actuator)
            db.session.commit()
        return redirect("/devices")

    @app.route("/register_device")
    @login_required
    def register_device():
        device_type = request.args.get("device_type", None)
        error_message = request.args.get("error_message", None)
        return render_template(
            "devices/register_device.html",
            error_message=error_message,
            device_type=device_type,
        )

    @app.route("/add_device", methods=["GET", "POST"])
    @login_required
    def add_device():
        if request.method == "POST":
            device_type = request.form["device_type"]
            device_name = request.form["device_name"]
            device_value = request.form["device_value"]
            kit_name = request.form["kit_name"]
            kit = Kit.select_kit_by_name(kit_name)
            device_topic = request.form["device_topic"]
            existing_device = Device.select_device_by_name(device_name)

            if not kit:
                return redirect(
                    url_for(".register_device", error_message="Esse kit não existe!")
                )
            elif existing_device:
                return redirect(
                    url_for(
                        ".register_device",
                        error_message="Esse dispositivo já existe",
                    )
                )
            else:
                kit_id = Kit.select_kit_by_name(kit_name).id
                if device_type == "actuator":
                    Actuator.insert_actuator(
                        kit_name, kit_id, device_name, device_value, device_topic
                    )
                elif device_type == "sensor":
                    Sensor.insert_sensor(
                        kit_name, kit_id, device_name, device_value, device_topic
                    )

                return redirect("/devices")

    @app.route("/publish_message", methods=["POST"])
    def publish_message():
        global ar_condicionado
        request_data = request.get_json()
        ar_condicionado = int(request_data["valor"])
        mqtt_client.publish("cz/degar", json.dumps(request_data))
        return jsonify({"success": True})

    @app.route("/real_time", methods=["GET", "POST"])
    def real_time():
        global temperature, people, last_update_dht, last_update_people, ar_condicionado
        people = people if people <= max_people_capacity else max_people_capacity
        people = people if people >= 0 else 0
        values = {"Temperatura": temperature, "Pessoas": people}

        return render_template(
            "real_time.html",
            values=values,
            user=session.get("user"),
            max_capacity=max_people_capacity,
            people=people,
            temperature=temperature,
            last_update_people=last_update_people,
            last_update_dht=last_update_dht,
            ar_condicionado=ar_condicionado,
        )

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Broker Connected successfully")
            mqtt_client.subscribe(topic_recive)
            mqtt_client.subscribe(topic_send)
            print("Broker Connected successfully")
        else:
            print("Bad connection. Code:", rc)

    @mqtt_client.on_disconnect()
    def handle_disconnect(client, userdata, rc):
        print("Disconnected from broker")

    # @app.errorhandler(404)
    # def page_not_found(error):
    #     logged = False
    #     if session.get("user"):
    #         logged = True
    #     return (
    #         render_template(
    #             "errors/error.html",
    #             error_message="Parece que a página não existe! Tente novamente!",
    #             logged=logged,
    #         ),
    #         404,
    #     )
    #
    # @app.errorhandler(405)
    # def page_not_found(error):
    #     return (
    #         render_template("errors/error.html", error_message="Você não fez login!"),
    #         405,
    #     )

    @login_manager.request_loader
    def load_user_from_request(request):

        # first, try to login using the api_key url arg
        api_key = request.args.get("api_key")
        if api_key:
            user = User.query.filter_by(api_key=api_key).first()
            if user:
                return user

        # next, try to login using Basic Auth
        api_key = request.headers.get("Authorization")
        if api_key:
            api_key = api_key.replace("Basic ", "", 1)
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
