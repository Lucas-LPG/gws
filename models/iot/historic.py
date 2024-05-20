from models.db import db
from models.iot.devices import Device

class Historic(db.Model):
    __tablename__ = 'historic'
    id = db.Column('id', db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    devices_id = db.Column(db.Integer, db.ForeignKey(Device.id))
    datetime = db.Column(db.DateTime)
    
    def __init__(self, valor, datetime, devices_id):
        self.valor = valor
        self.datetime = datetime
        self.devices_id = devices_id