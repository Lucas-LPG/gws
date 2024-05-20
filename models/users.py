from models import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    password = db.Column(VARCHAR(20), nullable=False)
    login = db.Column(VARCHAR(200), nullable=False)
    role = db.Column(VARCHAR(20), nullable=False)
    
    def __init__(self, password, login, role):
        self.password = password
        self.login = login
        self.role = role