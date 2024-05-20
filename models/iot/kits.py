from models.db import db
from models.iot.users import User

class Kit(db.Model):
    __tablename__ = 'kits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users_id = db.Column(db.Integer, db.ForeignKey(User.id))
    
    def __init__(self, name, users):
        self.name = name
        self.users = users
        