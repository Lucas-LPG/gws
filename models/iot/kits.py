from models.db import db
from models.iot.users import User
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

class Kit(db.Model):
    __tablename__ = 'kits'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(VARCHAR(100), nullable=False)
    user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(User.id))
    
    def __init__(self, name, users, user_id):
        self.name = name
        self.users = users
        self.user_id = user_id
        