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
from controllers.app_controller import create_app
import json


if __name__ == "__main__":
    app = create_app();
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(sensor, url_prefix='/')
    app.register_blueprint(actuator, url_prefix='/')    
    app.run(host='0.0.0.0', port=8080, debug=True),
