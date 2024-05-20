from models import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(VARCHAR(200), nullable=False)
    password = db.Column(VARCHAR(200), nullable=False)
    role = db.Column(VARCHAR(20), nullable=False)
    
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role