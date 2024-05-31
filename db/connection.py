from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists

db = SQLAlchemy()

user = "lucas"
password = "lucas"
server = "localhost"
port = 3306
database = "puhl_gasperin_health"

instance = f"mysql+pymysql://{user}:{password}@{server}:{port}/{database}"

if not database_exists(url=instance):
    create_database(url=instance)
