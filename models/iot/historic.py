from models.db import db

#FIXME: Não cria essa classe
class Historic(db.Model):
    __tablename__ = 'historic'
    id = db.Column('id', db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, valor, datetime):
        self.valor = valor
        self.datetime = datetime