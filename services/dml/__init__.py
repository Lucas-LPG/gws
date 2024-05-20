from flask import Flask
from models.users import User
from models import db

def populate_users(app:Flask):
    with app.app_context():
        session = db.session
        users = [
            User('lucas', 'pucas', 'admin'),
            User('tiago', 'gaspe' , 'estagiario'),
            User('Yuji Itadori', 'jujutsu_sorcerer', 'student'),
            User('Megumi Fushiguro', 'divine_dogs', 'student'),
            User('Aoi Todo', 'boogie_woogie', 'student'),
            User('Satoru Gojo', 'limitless', 'teacher'),
            User('Sukuna', 'king_of_curses', 'curse'),
            User('Monkey D. Luffy', 'gomu_gomu', 'pirate captain'),
            User('Roronoa Zoro', 'three_swords', 'swordsman'),
            User('Nami', 'navigation_expert', 'navigator'),
            User('Usopp', 'sogeking', 'sniper'),
            User('Sanji', 'black_leg', 'cook'),
            User('Tony Tony Chopper', 'doctorine', 'doctor')
        ]
        
        session.add_all(users)
        session.commit()

    

def populate_db(app: Flask):
    populate_users(app)