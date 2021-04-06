from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qxbazulxnsppso:d1ea93932f699a54e2b0ecf413b9309191c5b4dec83b7f5c983dc347b038e179@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d4em91gppr7mcf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Instancia o sqlalchemy usando as configurações acima
db: SQLAlchemy

class Cliente(db.Model):
    __tablename__ = 'cliente'
    cliente_id = db.Column(db.Integer, db.Sequence(
        'cliente_id_auto_incremento', start=1), primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String)
    dataNasc = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    telefone = db.Column(db.String)
    foto = db.Column(db.LargeBinary)
    
    


class Autonomo(db.Model):
    __tablename__ = 'autonomo'
    autonomo_id = db.Column(db.Integer, db.Sequence(
        'autonomo_id_auto_incremento', start=1), primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String)
    dataNasc = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    telefone = db.Column(db.String)
    foto = db.Column(db.LargeBinary)
    plano = db.Column(db.Integer)
    categoria = db.Column(db.String)
    valorhora = db.Column(db.Float)
    pedidos = db.Column(db.Integer)
    descricao = db.Column(db.String)
    classificacao = db.Column(db.Float)

class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    portfolio_id = db.Column(db.Integer, db.Sequence(
        'portfolio_id_auto_incremento', start=1), primary_key=True)
    id_usuario = db.Column(db.Integer)
    foto = db.Column(db.LargeBinary)

class Classificacao(db.Model):
    __tablename__ = 'classificacao'
    classificacao_id = db.Column(db.Integer, db.Sequence(
        'classificacao_id_auto_incremento', start=1), primary_key=True)
    id_usuario = db.Column(db.Integer)
    nota = db.Column(db.Float)

db.drop_all()
db.create_all()
# postgresql://qxbazulxnsppso:d1ea93932f699a54e2b0ecf413b9309191c5b4dec83b7f5c983dc347b038e179@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d4em91gppr7mcf