from db.connection import db
from models.devices import Device
from models.kits import Kit
from models.users import User
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class Sensor(db.Model):
    __tablename__ = 'sensors'
    id = db.Column('id', INTEGER(unsigned=True),
                   primary_key=True, autoincrement=True)
    topic = db.Column(VARCHAR(50), nullable=False)
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    @classmethod  # define que é um metodo da classe, permitindo acessar e manipular atributos e metodos da classe
    def insert_sensor(cls, kit_name, kit_id, user_id, device_name, value, topic):

        id_verification = db.session.query(User).filter_by(id=user_id).first()
        kit_verification = db.session.query(Kit).filter_by(id=kit_id).first()
        if not id_verification:
            print(f"O id {user_id} nao existe, por favor insira outro")
        #    return
        else:
            if not kit_verification:
                kit = Kit(name=kit_name, user_id=user_id)
                db.session.add(kit)
                db.session.commit()

                device = Device(name=device_name, value=value, kit_id=kit.id)
                db.session.add(device)
                db.session.commit()

                sensor = Sensor(topic, device_id=device.id)
                db.session.add(sensor)
                db.session.commit()

            else:
                device = Device(name=device_name, value=value, kit_id=kit.id)
                db.session.add(device)
                db.session.commit()

                sensor = Sensor(topic, device_id=device.id)
                db.session.add(sensor)
                db.session.commit()

    @classmethod
    def select_all_from_sensor(cls):
        sensors = (
            Sensor.query.join(Device, Device.id == Sensor.device_id)
            .join(Kit, Kit.id == Device.kit_id)
            .join(User, User.id == Kit.user_id)
            .add_columns(
                User.name.label('user_name'),
                Kit.name.label('kit_name'),
                Device.name.label('device_name'),
                Device.value.label('device_value'),
                Sensor.id.label('id'),
                Sensor.topic.label('topic'),
                Device.id.label("device_id")).all()
        )
        return sensors

    def select_from_sensors(condition):
        sensors = db.session.query(Sensor).filter(condition).all()
        return sensors

    @classmethod
    def update_sensor_by_id(cls, sensor_id, name, value, topic):
        sensor = db.session.query(Sensor).filter_by(id=sensor_id).first()
        if not sensor:
            print("O id nao existe, insira outro")

        else:
            device = db.session.query(Device).filter_by(
                id=sensor.device_id).first()

            if device is not None:
                device.name = name
                device.value = value
                sensor.topic = topic
                db.session.commit()

    @classmethod  # define que é um metodo da classe, para poder editar variaveis dela
    def delete_sensor_by_id(cls, sensor_id):
        device = db.session.query(Device).filter_by(id=sensor_id).first()
        db.session.delete(device)
        db.session.commit()

    def __init__(self, topic, device_id):
        self.topic = topic
        self.device_id = device_id
