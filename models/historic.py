from sqlalchemy.dialects.mysql import DATETIME, FLOAT, INTEGER
from sqlalchemy.sql import func

from db.connection import db
from models.devices import Device


class Historic(db.Model):
    __tablename__ = "historic"
    id = db.Column("id", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    value = db.Column(FLOAT, nullable=False)
    datetime = db.Column(DATETIME, nullable=False, default=func.now())
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    def select_all_from_historic():
        from models.devices import Device
        from models.kits import Kit
        from models.users import User

        # user_name, kit_name, device_name, value, datatime

        historic = (
            Historic.query.join(Device, Device.id == Historic.device_id)
            .join(Kit, Kit.id == Device.kit_id)
            .join(User, User.id == Kit.user_id)
            .add_columns(
                User.name.label("user_name"),
                Kit.name.label("kit_name"),
                Device.name.label("device_name"),
                Historic.value.label("device_value"),
                Historic.datetime.label("device_datetime"),
            )
        )

        return historic

    def select_by_datetime_from_historic(datetime_start, datetime_end):
        from models import Kit

        historic = (
            Historic.query.join(Device, Device.id == Historic.device_id)
            .join(Kit, Kit.id == Device.kit_id)
            .filter(
                Historic.datetime > datetime_start, Historic.datetime < datetime_end
            )
            .add_columns(
                Historic.value.label("historic_value"),
                Historic.datetime.label("historic_datetime"),
                Device.name.label("device_name"),
                Kit.name.label("kit_name"),
            )
            .all()
        )
        return historic

    def select_datetime_by_device_id(historic_device_id):
        device_historic = (
            db.session.query(func.max(Historic.datetime))
            .filter_by(device_id=historic_device_id)
            .scalar()
        )
        return device_historic

    def select_historic_by_device_id(historic_device_id):
        historic = (
            db.session.query(Historic).filter_by(device_id=historic_device_id).first()
        )
        if historic is not None:
            return historic

    def last_update_datetime(datetime_last_update):
        difference = db.session.query(func.now() - datetime_last_update).all()
        for result in difference:
            print(result)

        return difference

    def __init__(self, value, datetime, device_id):
        self.value = value
        self.datetime = datetime
        self.device_id = device_id
