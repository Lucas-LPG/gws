# app.py
from controllers import create_app
from controllers.actuators import actuator
from controllers.login import login
from controllers.sensors import sensor
from db import create_db
from db.connection import db, instance

if __name__ == "__main__":
    app = create_app()
    app.config["TESTING"] = False
    app.config["SECRET_KEY"] = "senha_forte-Lucas-puCas12"
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)
    create_db(app)
    app.register_blueprint(login, url_prefix="/")
    app.register_blueprint(sensor, url_prefix="/")
    app.register_blueprint(actuator, url_prefix="/")
    app.run(host="0.0.0.0", port=8080, debug=True),
