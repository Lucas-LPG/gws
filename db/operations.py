from flask import Flask
from db.connection import db
from sqlalchemy import select, update, insert
from models.actuators import Actuator
from models.devices import Device
from models.historic import Historic
from models.kits import Kit
from models.sensors import Sensor
from models.users import User

session = db.session

def insert_db(app: Flask, obj):
    with app.app_context():
        # Garantir que nome de usuário não exista ainda
        if isinstance(obj, User):
            if select_db(app, User, (User.name == obj.name)) == []:
                try:
                    db.session.add(obj)
                    db.session.commit()
                    print(f'O usuário {obj.name} foi adicionado com sucesso!')
                except ValueError as ve:
                    print(f"Erro: {ve}")
                    db.session.rollback()
                except Exception as e:
                    # print(f"Ocorreu um erro: {e}")
                    db.session.rollback()
            else:
                print(f'O nome de usuário {obj.name} já existe! Tente novamente com um novo.')
        else:
            try:
                db.session.add(user)
                db.session.commit()
            except ValueError as ve:
                print(f"Erro: {ve}")
                db.session.rollback()
            except Exception as e:
                # print(f"Ocorreu um erro: {e}")
                db.session.rollback()
                
def select_db(app:Flask, column, condition):
    
    query = select(column)
    if condition != '':
        query = select(column).where(condition)
    
    result = []
    with app.app_context():
        for entity in session.execute(query).scalars():
            result.append(entity)
    
    return result