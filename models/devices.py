from db.connection import db
from models.kits import Kit
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, FLOAT


class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column('id', INTEGER(unsigned=True),
                   primary_key=True, autoincrement=True)
    name = db.Column(VARCHAR(100), nullable=False)
    value = db.Column(FLOAT, nullable=False)
    kit_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(Kit.id))

    # nao sei se precisa dessa funcao, vou ir testando e vendo ate onde chego

    # def insert_into_devices(name, value, kit_id):
    #     kit  = Kit()
    #     device = Device(name, value, kit_id)

    #     db.session.add(device)
    #     db.session.commit()

    def __init__(self, name, value, kit_id):
        self.name = name
        self.value = value
        self.kit_id = kit_id
