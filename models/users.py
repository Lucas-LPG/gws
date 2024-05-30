from flask_login import UserMixin
from sqlalchemy import CheckConstraint
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

from db.connection import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column("id", INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(VARCHAR(200), nullable=False, unique=True)
    password = db.Column(VARCHAR(200), nullable=False)
    role = db.Column(VARCHAR(20), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'estatistico', 'operador')", name="check_role"
        ),
    )

    def validate_user(name, password):
        return User.query.filter_by(name=name, password=password).first()

    def insert_into_users(name, password, role):
        user = User(name, password, role)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def select_all_information_from_users(cls):
        from models.kits import Kit

        users = (
            User.query.outerjoin(Kit, Kit.user_id == User.id)
            .add_columns(
                User.name.label("user_name"),
                User.role.label("role"),
                User.id.label("user_id"),
                Kit.name.label("kit_name"),
            )
            .all()
        )

        return users

    def select_from_users(condition):
        users = db.session.query(User).filter(condition).all()
        return users

    def select_user_by_id(user_id):
        user = db.session.query(User).filter_by(id=user_id).first()
        if user is not None:
            return user

    @classmethod
    def delete_user_by_id(cls, user_id):
        user = db.session.query(User).filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

    def __init__(self, name, password, role):
        # if roge not in ("admin", "estatistico", "operador"):
        #     print(
        #         f'\nFalha ao adicionar usuário: {
        #             name} \nO campo role deve ser "admin", "estatistico" ou "operador"\n'
        #     )
        self.name = name
        self.password = password
        self.role = role
