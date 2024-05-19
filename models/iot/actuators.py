from models.db import db
from models.iot.devices import Device

#FIXME: Não cria essa classe
class Actuator(db.Model):
    __tablename__ = 'actuators'
    id = db.Column('id', db.Integer, primary_key=True)
    devices_id = db.Column( db.Integer, db.ForeignKey(Device.id))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))
    
    def __init__(self, devices_id, unit, topic):
        self.devices_id = devices_id
        self.unit = unit
        self.topic = topic