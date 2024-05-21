from flask import Flask
from services.dml.initial_insert import populate_users, populate_kits, populate_actuators, populate_devices, populate_sensors
from services.dml.interact import insert_db


def populate_db(app: Flask):
    populate_users(app)
    populate_kits(app)
    populate_devices(app)
    populate_actuators(app)
    populate_sensors(app)
