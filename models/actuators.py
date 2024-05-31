from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from db.connection import db
from models.devices import Device
from models.kits import Kit
from models.users import User


class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("id", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    topic = db.Column(VARCHAR(50), nullable=False)
    device_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Device.id))

    def insert_actuator(kit_name, kit_id, device_name, value, topic):

        existing_device = Device.select_device_by_name(device_name)

        if existing_device:
            actuator = Actuator(topic, device_id=existing_device.id)
        else:
            device = Device(name=device_name, value=value, kit_id=kit_id)
            db.session.add(device)
            db.session.commit()

            actuator = Actuator(topic, device_id=device.id)
            db.session.add(actuator)
            db.session.commit()

    def select_all_from_actuators():
        actuators = (
            db.session.query(
                Actuator.topic.label("actuator_topic"),
                Actuator.id.label("actuator_id"),
                Device.id.label("device_id"),
                Device.name.label("device_name"),
                Device.value.label("device_value"),
                Kit.name.label("kit_name"),
            )
            .join(Device, Actuator.device_id == Device.id)
            .outerjoin(Kit, Device.kit_id == Kit.id)
            .group_by(Device.id, Actuator.topic, Actuator.id, Device.name, Kit.name)
            .all()
        )
        return actuators

    def update_given_actuator(
        given_device_id, device_id, device_name, device_value, device_topic, kit_name
    ):
        device = db.session.query(Device).filter_by(id=device_id).first()
        actuator = db.session.query(Actuator).filter_by(id=given_device_id).first()
        kit = db.session.query(Kit).filter_by(name=kit_name).first().id

        if device is not None:
            device.name = device_name
            device.value = device_value
            device.kit_id = kit

        if actuator is not None:
            actuator.topic = device_topic
            actuator.device_id = device_id

        db.session.commit()

    def update_actuator_by_id(actuator_id, name, value, topic):
        actuator = db.session.query(Actuator).filter_by(id=actuator_id).first()
        if not actuator:
            print("O id nao existe, insira outro")
        else:
            device = db.session.query(Device).filter_by(id=actuator.device_id).first()

            if device is not None:
                device.name = name
                device.value = value
                actuator.topic = topic
                db.session.commit()

    # def select_topic_by_user_id(user_id):
    #     topic = (
    #         Actuator.query.join(Device, Device.id == Actuator.device_id)
    #         .join(Kit, Kit.id == Device.kit_id)
    #         .join(User, User.id == Kit.user_id)
    #         .join(User, User.id == user_id)
    #         .add_column(
    #             Actuator.topic.label("topic")
    #         )
    #         .all()
    #     )
    #     return topic
    def select_actuators_by_id(device_id):
        actuators = (
            db.session.query(
                Actuator.topic.label("device_topic"),
                Actuator.id.label("actuator_id"),
                Device.id.label("device_id"),
                Device.name.label("device_name"),
                Device.value.label("device_value"),
                Kit.name.label("kit_name"),
            )
            .filter(Actuator.device_id == device_id)
            .join(Device, Actuator.device_id == Device.id)
            .outerjoin(Kit, Device.kit_id == Kit.id)
            .group_by(Device.id, Actuator.topic, Actuator.id, Device.name, Kit.name)
            .first()
        )
        return actuators

    def select_single_actuator_by_id(id):
        actuator = db.session.query(Actuator).filter_by(id=id).first()
        if actuator is not None:
            return actuator

    def select_device_by_actuator_id(actuator_id):
        actuator = db.session.query(Actuator).filter_by(id=actuator_id).first()
        device = db.session.query(Device).filter_by(id=actuator.device_id).first()
        if device is not None:
            return device

    @classmethod
    def update_actuator_button_value(cls, device_id, new_value):
        actuator = db.session.query(Device).filter_by(id=device_id).first()
        actuator.value += new_value
        db.session.commit()

    def delete_actuator_by_id(actuator_id):
        device = db.session.query(Device).filter_by(id=actuator_id).first()
        db.session.delete(device)
        db.session.commit()

    def __init__(self, topic, device_id):
        self.topic = topic
        self.device_id = device_id
