from flask import Flask
from models.users import User
from models import db

def populateUsers(app:Flask):
    with app.app_context():
        session = db.session
        users = [
            User('lucas', 'pucas', 'admin'),
            User('tiago', 'gaspe' , 'estagiario'),
            User('frank', '2c7e9ca978dfd994d56f4e0cf534062d631484d2', 'professor')
        ]
        
        session.add_all(users)
        session.commit()


    

def populateDb():
    populateUsers(app)