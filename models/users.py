from db.connection import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy import CheckConstraint

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(VARCHAR(200), nullable=False, unique=True)
    password = db.Column(VARCHAR(200), nullable=False)
    role = db.Column(VARCHAR(20), nullable=False)
    
    __table_args__ = (
        CheckConstraint("role IN ('admin', 'estatistico', 'operador')", name='check_role'),
    )
    
    def __init__(self, name, password, role):
        if role not in ('admin', 'estatistico', 'operador'):
            print(f'\nFalha ao adicionar usuário: {name}\nO campo role deve ser "admin", "estatistico" ou "operador"\n')
        self.name = name
        self.password = password
        self.role = role
