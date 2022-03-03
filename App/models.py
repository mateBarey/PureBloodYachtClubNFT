from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "tokens"
    email = db.Column(db.String(32), primary_key=True, unique=True, nullable=True)
    password = db.Column(db.String(32), nullable=False, unique=True)
    eth_address = db.Column(db.String(32), nullable=False, unique=True)