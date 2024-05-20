from models.db import db
from models.iot.devices import Device
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class Actuator(db.Model):
    __tablename__ = 'actuators'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    unit = db.Column(VARCHAR(50), nullable=False)
    topic = db.Column(VARCHAR(50), nullable=False)
    device_id = db.Column( INTEGER(unsigned=True), db.ForeignKey(Device.id))
    
    def __init__(self,  unit, topic, devices_id):
        self.unit = unit
        self.topic = topic
        self.devices_id = devices_id