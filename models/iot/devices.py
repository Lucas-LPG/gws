from models.db import db
from models.iot.kits import Kit

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.Float)
    kit_id = db.Column(db.Integer, db.ForeignKey(Kit.id))
    
    def __init__(self, name, value, kit_id):
        self.name = name
        self.value = value
        self.kit_id = kit_id