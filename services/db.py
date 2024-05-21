from flask import Flask
from models import *
from services.sql.initiate_db import initiate_db
from services.sql.events import create_historic_trigger


def create_db(app: Flask):
    with app.app_context():
        initiate_db(app)
        db.drop_all()
        db.create_all()
        create_historic_trigger(app)
