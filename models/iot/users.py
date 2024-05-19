from models.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.VARCHAR(20))
    login = db.Column(db.VARCHAR(200))
    role = db.Column(db.VARCHAR(20))
    
    def __init__(self, password, login, role):
        self.password = password
        self.login = login
        self.role = role