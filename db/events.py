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


def handle_device_deletion(app:Flask):
    """
    TODO: Devemos pensar em como lidar com entidades com foreign keys deletadas
    Por exemplo, se device 1 for apagado, o histórico dele deve ser apagado também?
    Se user 1 for apagado, o kit relacionado a ele deve ter o que de user_id?
    """
    trigger = DDL("""
       CREATE TRIGGER delete_sensors_before_devices
       BEFORE DELETE ON devices
       FOR EACH ROW
       BEGIN
       DELETE FROM sensors WHERE id == OLD.id
       DELETE FROM actuators WHERE id == OLD.id
       END
    """)