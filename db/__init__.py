from flask import Flask
from models import *
from .clean_db import clean_db
from .events import create_historic_trigger, handle_device_deletion, handle_kit_deletion, handle_user_deletion, update_historic_trigger
from .initial_insert import initial_populate_db
from .connection import db


def create_db(app: Flask):
    with app.app_context():
        clean_db(app)
        db.drop_all()
        db.create_all()
        create_historic_trigger(app)
        update_historic_trigger(app)
        handle_device_deletion(app)
        handle_user_deletion(app)
        handle_kit_deletion(app)
        initial_populate_db(app)
