from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)  # Instancia o sqlalchemy usando as configurações acima
# db: SQLAlchemy

class Cliente(db.Model):
    __tablename__ = 'cliente'
    cliente_id = db.Column(db.Integer, db.Sequence(
        'cliente_id_auto_incremento', start=1), primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String)
    dataNasc = db.Column(db.DateTime)
    cpf = db.Column(db.String, unique=True)
    telefone = db.Column(db.String)
    foto = db.Column(db.BLOB)
    plano = db.Column(db.Integer)
    


class Autonomo(db.Model):
    __tablename__ = 'autonomo'
    autonomo_id = db.Column(db.Integer, db.Sequence(
        'autonomo_id_auto_incremento', start=1), primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String)
    dataNasc = db.Column(db.DateTime)
    cpf = db.Column(db.String, unique=True)
    telefone = db.Column(db.String)
    foto = db.Column(db.BLOB)
    plano = db.Column(db.Integer)
    categoria = db.Column(db.String)
    valorhora = db.Column(db.Numeric(precision=10, scale=2))
    pedidos = db.Column(db.Integer)
    descricao = db.Column(db.String)
    classificacao = db.Column(db.Numeric(precision=10, scale=2))

class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    portfolio_id = db.Column(db.Integer, db.Sequence(
        'portfolio_id_auto_incremento', start=1), primary_key=True)
    id_usuario = db.Column(db.Integer)
    foto = db.Column(db.BLOB)

class Classificacao(db.Model):
    __tablename__ = 'classificacao'
    classificacao_id = db.Column(db.Integer, db.Sequence(
        'classificacao_id_auto_incremento', start=1), primary_key=True)
    id_usuario = db.Column(db.Integer)
    nota = db.Column(db.Numeric(precision=10, scale=2))

db.drop_all()
db.create_all()