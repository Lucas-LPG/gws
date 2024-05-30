from sqlalchemy import func
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from db.connection import db
from models.users import User


class Kit(db.Model):
    __tablename__ = "kits"
    id = db.Column("id", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(VARCHAR(100), nullable=False)
    user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(User.id))

    def select_all_from_kits():
        # Previnir circular import
        from models.actuators import Actuator
        from models.devices import Device
        from models.sensors import Sensor

        kits = (
            db.session.query(
                Kit.id.label("kit_id"),
                Kit.name.label("kit_name"),
                User.name.label("user_name"),
                func.count(func.distinct(Sensor.id)).label("total_sensors"),
                func.count(func.distinct(Actuator.id)).label("total_actuators"),
            )
            .join(User, Kit.user_id == User.id)
            .outerjoin(Device, Device.kit_id == Kit.id)
            .outerjoin(Sensor, Sensor.device_id == Device.id)
            .outerjoin(Actuator, Actuator.device_id == Device.id)
            .group_by(Kit.id, User.name)
            .all()
        )
        return kits

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
