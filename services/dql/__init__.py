from flask import Flask
from models import db
from models.actuators import Actuator
from models.devices import Device
from models.historic import Historic
from models.kits import Kit
from models.sensors import Sensor
from models.users import User

from sqlalchemy import select, update, insert

session = db.session

def select_db(app:Flask, column, condition):
    
    query = select(column)
    if condition != '':
        query = select(column).where(condition)
    
    result = []
    with app.app_context():
        for entity in session.execute(query).scalars():
            result.append(entity)
    
    return result


            