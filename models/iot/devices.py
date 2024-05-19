from models.db import db

class Device(db.Model):
    __tablename__ = 'devices'
    id= db.Column('id', db.Integer, primary_key=True)
    name= db.Column(db.String(50))
    brand= db.Column(db.String(50))
    model= db.Column(db.String(50))
    is_active= db.Column(db.Boolean, nullable= False, default= False)