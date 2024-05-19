from models.db import db
from models.iot.devices import Device
from models.iot.sensors import Sensor
sensors = db.relationship('Sensor', backref='devices', lazy=True)
