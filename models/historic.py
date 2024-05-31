from db.connection import db
from sqlalchemy.dialects.mysql import INTEGER, FLOAT, DATETIME
from models.devices import Device
from sqlalchemy.sql import func, desc


class Historic(db.Model):
    __tablename__ = 'historic'
    id = db.Column('id', INTEGER(unsigned=True),
                   primary_key=True, autoincrement=True)
    value = db.Column(FLOAT, nullable=False)
    datetime = db.Column(DATETIME, nullable=False, default=func.now())
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    def select_all_from_historic():
        from models.users import User
        from models.kits import Kit
        from models.devices import Device

        # user_name, kit_name, device_name, value, datatime

        historic = (

            Historic.query.join(Device, Device.id == Historic.device_id)
            .join(Kit, Kit.id == Device.kit_id)
            .add_columns(
                Kit.name.label('kit_name'),
                Device.name.label('device_name'),
                Historic.value.label('device_value'),
                Historic.datetime.label('device_datetime')
            )

        )

        return historic

    def select_by_datetime_from_historic(datetime_begin, datetime_end):
        from models import Kit
        historic = (
            Historic.query.join(Device, Device.id == Historic.device_id)
            .join(Kit, Kit.id == Device.kit_id)
            .filter(Historic.datetime > datetime_begin,
                    Historic.datetime < datetime_end)
            .add_columns(
                Historic.value.label("device_value"),
                Historic.datetime.label("device_datetime"),
                Device.name.label("device_name"),
                Kit.name.label("kit_name")
            )
            .order_by(desc(Historic.datetime))
            .all()

        )
        return historic

    def select_datetime_by_device_id(historic_device_id):
        device_historic = db.session.query(func.max(Historic.datetime)).filter_by(
            device_id=historic_device_id).scalar()
        return device_historic

    def select_historic_by_device_id(historic_device_id):
        historic = db.session.query(Historic).filter_by(
            device_id=historic_device_id).first()
        if historic is not None:
            return historic

    def __init__(self, value, datetime, device_id):
        self.value = value
        self.datetime = datetime
        self.device_id = device_id
