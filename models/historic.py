from models import db
from sqlalchemy.dialects.mysql import INTEGER, FLOAT, DATETIME
from models.devices import Device
from sqlalchemy.sql import func

class Historic(db.Model):
    __tablename__ = 'historic'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    value = db.Column(FLOAT, nullable=False)
    datetime = db.Column(DATETIME, nullable=False, default=func.now())
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))
    
    def __init__(self, value, datetime, device_id):
        self.value = value
        self.datetime = datetime
        self.device_id = device_id