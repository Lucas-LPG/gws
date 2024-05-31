from db.connection import db
from sqlalchemy.dialects.mysql import INTEGER, FLOAT, DATETIME
from models.devices import Device
from sqlalchemy.sql import func


class Historic(db.Model):
    __tablename__ = 'historic'
    id = db.Column('id', INTEGER(unsigned=True),
                   primary_key=True, autoincrement=True)
    value = db.Column(FLOAT, nullable=False)
    datetime = db.Column(DATETIME, nullable=False, default=func.now())
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    def select_all_from_historyc():
        from models.users import User
        from models.kits import Kit
        from models.devices import Device

        # user_name, kit_name, device_name, value, datatime

        historic = (

            Historic.query.join(Device, Device.id == Historic.device_id)
            .join(Kit, Kit.id == Device.kit_id)
            .join(User, User.id == Kit.user_id)
            .add_columns(
                User.name.label('user_name'),
                Kit.name.label('kit_name'),
                Device.name.label('device_name'),
                Historic.value.label('device_value'),
                Historic.datetime.label('device_datetime')
            )

        )

        return historic

    def __init__(self, value, datetime, device_id):
        self.value = value
        self.datetime = datetime
        self.device_id = device_id
