from models import db
from sqlalchemy.dialects.mysql import INTEGER, FLOAT, DATETIME
from models.devices import Device
from sqlalchemy.sql import func

class Historic(db.Model):
    __tablename__ = 'historic'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    valor = db.Column(FLOAT, nullable=False)
    datetime = db.Column(DATETIME, nullable=False, default=func.now())
    devices_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))
    
    def __init__(self, valor, datetime, devices_id):
        self.valor = valor
        self.datetime = datetime
        self.devices_id = devices_id