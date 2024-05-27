from db.connection import db
from models.devices import Device
from models.kits import Kit
from models.users import User
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class Actuator(db.Model):
    __tablename__ = 'actuators'
    id = db.Column('id', INTEGER(unsigned=True),
                   primary_key=True, autoincrement=True)
    topic = db.Column(VARCHAR(50), nullable=False)
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    def insert_actuator(kit_name, user_id, device_name, value, topic):
        id_verification = db.session.query(User).filter_by(id=user_id).first()
        if not id_verification:
            print(f"O id {user_id} nao existe, por favor insira outro")
        else:
            kit = Kit(name=kit_name, user_id=user_id)

            db.session.add(kit)
            db.session.commit()

            device = Device(name=device_name, value=value, kit_id=kit.id)
            db.session.add(device)
            db.session.commit()

            actuator = Actuator(topic, device_id=device.id)
            db.session.add(actuator)
            db.session.commit()

    def select_all_from_actuator():
        actuator = Actuator.query.join(Device, Device.id == Actuator.device_id).join(Kit, Kit.id == Device.kit_id).join(User, User.id == Kit.user_id)\
            .add_columns(User.name.label('user_name'),
                         Kit.name.label('kit_name'),
                         Device.name.label('device_name'),
                         Device.value.label('device_value'),
                         Actuator.id.label('id'),
                         Actuator.topic.label('topic'),
                         Device.id.label('device_id')).all()
        return actuator

    def delete_actuator_by_id(actuator_id):
        device = db.session.query(Device).filter_by(id=actuator_id).first()
        db.session.delete(device)
        db.session.commit()

    def __init__(self, topic, device_id):
        self.topic = topic
        self.device_id = device_id
