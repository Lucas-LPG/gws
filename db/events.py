from flask import Flask
from sqlalchemy import DDL
from db.connection import db
from models.devices import Device

session = db.session


def create_historic_trigger(app: Flask):
    trigger = DDL("""
        CREATE TRIGGER create_historic
        AFTER INSERT ON devices
        FOR EACH ROW
        BEGIN
        INSERT INTO historic(value, datetime, device_id) VALUES(NEW.value, NOW(), NEW.id);
        END;
                  """
                  )

    session.execute(trigger)


def update_historic_trigger(app: Flask):
    trigger = DDL("""
        CREATE TRIGGER update_historic
        AFTER UPDATE ON devices
        FOR EACH ROW
        BEGIN
        INSERT INTO historic(value, datetime, device_id) VALUES(NEW.value, NOW(), NEW.id);
        END;
                  """
                  )

    session.execute(trigger)


def handle_device_deletion(app: Flask):
    """
    TODO: Devemos pensar em como lidar com entidades com foreign keys deletadas
    Por exemplo, se device 1 for apagado, o histórico dele deve ser apagado também?
    Se user 1 for apagado, o kit relacionado a ele deve ter o que de user_id?

    Boa pergunta gasp!

    Ideia do tiago: 
    se for deletar user
        tudo, absolutamente tudo relacionado a ele é deletado
    se for deletar um device
        tira do kit e historico
    """
    trigger = DDL("""
       CREATE TRIGGER delete_sensors_or_actuators_before_devices
       BEFORE DELETE ON devices
       FOR EACH ROW
       BEGIN
        DELETE FROM sensors WHERE device_id = OLD.id;
        DELETE FROM actuators WHERE device_id = OLD.id;
        DELETE FROM historic WHERE device_id = OLD.id;
       END;
    """)
    session.execute(trigger)


def handle_user_deletion(app: Flask):
    trigger = DDL("""
        CREATE TRIGGER delete_kit_before_users
        BEFORE DELETE ON users
        FOR EACH ROW
        BEGIN
            DELETE FROM kits WHERE user_id = OLD.id;
        END;
    """)
    session.execute(trigger)


def handle_kit_deletion(app: Flask):
    trigger = DDL("""
        CREATE TRIGGER delete_device_before_kits
        BEFORE DELETE ON kits
        FOR EACH ROW
        BEGIN
            DELETE FROM devices WHERE kit_id = OLD.id;
        END;
    """)
    session.execute(trigger)
