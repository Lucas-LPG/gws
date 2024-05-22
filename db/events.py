from flask import Flask
from sqlalchemy import DDL
from db.connection import db
from models.devices import Device

session = db.session


def create_historic_trigger(app: Flask):
    trigger = DDL("""
        CREATE TRIGGER populate_historic
        AFTER INSERT ON devices
        FOR EACH ROW
        BEGIN
        INSERT INTO historic(value, datetime, device_id) VALUES(NEW.value, NOW(), NEW.id);
        END;
                  """
                  )

    session.execute(trigger)
