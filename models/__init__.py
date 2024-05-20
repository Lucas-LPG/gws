from models.db import db
from models.iot.devices import Device
from models.iot.sensors import Sensor
from models.iot.actuators import Actuator
from models.iot.historic import Historic

sensors = db.relationship('Sensor', backref='devices', lazy=True)
actuators = db.relationship('Actuator', backref='devices', lazy=True)
historic = db.relationship('Historic', backref='devices', lazy=True)