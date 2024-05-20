from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

user = "lucas"
password = "lucas"
server = "localhost"
port = 3306
database = "puhl_gasperin_health"

instance = f"mysql+pymysql://{user}:{password}@{server}:{port}/{database}"

if not database_exists(url=instance):
    create_database(url=instance)
    
from models.devices import Device
from models.sensors import Sensor
from models.actuators import Actuator
from models.historic import Historic
from models.users import User
from models.kits import Kit

# sensors = db.relationship('Sensor', backref='devices', lazy=True)
# actuators = db.relationship('Actuator', backref='devices', lazy=True)
# historic = db.relationship('Historic', backref='devices', lazy=True)