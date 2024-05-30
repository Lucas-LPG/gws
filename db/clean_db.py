from flask import Flask
from sqlalchemy import text
from db.connection import db

session = db.session

def clean_db(app: Flask):
    with app.app_context():
        drop_database_stmt = text('DROP DATABASE IF EXISTS puhl_gasperin_health;')
        session.execute(drop_database_stmt)

        create_database_stmt = text('CREATE DATABASE puhl_gasperin_health;')
        session.execute(create_database_stmt)

        use_database_stmt = text('USE puhl_gasperin_health;')
        session.execute(use_database_stmt)

        drop_user_stmt = text("DROP USER IF EXISTS 'lucas'@'%';")
        session.execute(drop_user_stmt)

        create_user_stmt = text('CREATE USER lucas IDENTIFIED BY "lucas";')
        session.execute(create_user_stmt)

        grant_stmt = text('GRANT ALL ON *.* TO lucas WITH GRANT OPTION;')
        session.execute(grant_stmt)

    