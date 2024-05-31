from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from db.connection import db
from models.devices import Device
from models.kits import Kit
from models.users import User


class Sensor(db.Model):
    __tablename__ = "sensors"
    id = db.Column("id", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    topic = db.Column(VARCHAR(50), nullable=False)
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    def insert_sensor(kit_name, kit_id, device_name, value, topic):

        existing_device = Device.select_device_by_name(device_name)

        if existing_device:
            sensor = Sensor(topic, device_id=existing_device.id)
        else:
            device = Device(name=device_name, value=value, kit_id=kit_id)
            db.session.add(device)
            db.session.commit()

            sensor = Sensor(topic, device_id=device.id)
            db.session.add(sensor)
            db.session.commit()

    def select_all_from_sensors():
        sensors = (
            db.session.query(
                Sensor.topic.label("sensor_topic"),
                Sensor.id.label("sensor_id"),
                Device.id.label("device_id"),
                Device.name.label("device_name"),
                Device.value.label("device_value"),
                Kit.name.label("kit_name"),
            )
            .join(Device, Sensor.device_id == Device.id)
            .outerjoin(Kit, Device.kit_id == Kit.id)
            .group_by(Device.id, Sensor.topic, Sensor.id, Device.name, Kit.name)
            .all()
        )
        return sensors

    def update_given_sensor(
        given_device_id, device_id, device_name, device_value, device_topic, kit_name
    ):
        device = db.session.query(Device).filter_by(id=device_id).first()
        sensor = db.session.query(Sensor).filter_by(id=given_device_id).first()
        kit = db.session.query(Kit).filter_by(name=kit_name).first().id

        if device is not None:
            device.name = device_name
            device.value = device_value
            device.kit_id = kit

        if sensor is not None:
            sensor.topic = device_topic
            sensor.device_id = device_id

        db.session.commit()

    def select_from_sensors(condition):
        sensors = db.session.query(Sensor).filter(condition).all()
        return sensors

    def select_single_sensor_by_id(id):
        sensor = db.session.query(Sensor).filter_by(id=id).first()
        if sensor is not None:
            return sensor

    @classmethod
    def update_sensor_by_id(cls, sensor_id, name, value, topic):
        sensor = db.session.query(Sensor).filter_by(id=sensor_id).first()
        if not sensor:
            print("O id nao existe, insira outro")

        else:
            device = db.session.query(Device).filter_by(id=sensor.device_id).first()

            if device is not None:
                device.name = name
                device.value = value
                sensor.topic = topic
                db.session.commit()

    def select_sensors_by_id(device_id):
        sensors = (
            db.session.query(
                Sensor.topic.label("device_topic"),
                Sensor.id.label("sensor_id"),
                Device.id.label("device_id"),
                Device.name.label("device_name"),
                Device.value.label("device_value"),
                Kit.name.label("kit_name"),
            )
            .filter(Sensor.id == device_id)
            .join(Device, Sensor.device_id == Device.id)
            .outerjoin(Kit, Device.kit_id == Kit.id)
            .group_by(Device.id, Sensor.topic, Sensor.id, Device.name, Kit.name)
            .first()
        )
        return sensors

    def select_device_by_sensor_id(sensor_id):
        sensor = db.session.query(Sensor).filter_by(id=sensor_id).first()
        device = db.session.query(Device).filter_by(id=sensor.device_id).first()
        if device is not None:
            return device

    @classmethod
    def update_sensor_value(cls, device_id, new_value):
        sensor = db.session.query(Device).filter_by(id=device_id).first()
        sensor.value = new_value
        db.session.commit()

    @classmethod  # define que é um metodo da classe, para poder editar variaveis dela
    def delete_sensor_by_id(cls, sensor_id):
        device = db.session.query(Device).filter_by(id=sensor_id).first()
        db.session.delete(device)
        db.session.commit()

    def __init__(self, topic, device_id):
        self.topic = topic
        self.device_id = device_id
