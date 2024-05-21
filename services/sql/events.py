from flask import Flask;
from sqlalchemy import DDL, event
from services.db import db
from models.devices import Device

session = db.session
def create_historic_trigger(app: Flask):
    event.listen(
    devices,
    "after_insert",
    DDL(
       "INSERT INTO historic(value, datetime, device_id) VALUES(NULL, NOW(), NEW.id);"
    )
)