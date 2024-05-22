from db.connection import db
from models.devices import Device
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class Actuator(db.Model):
    __tablename__ = 'actuators'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    topic = db.Column(VARCHAR(50), nullable=False)
    device_id = db.Column( INTEGER(unsigned=True), db.ForeignKey(Device.id))
    
    def __init__(self, topic, device_id):
        self.topic = topic
        self.device_id = device_id