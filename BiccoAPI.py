from flask import Flask, jsonify
from flask.globals import request
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qxbazulxnsppso:d1ea93932f699a54e2b0ecf413b9309191c5b4dec83b7f5c983dc347b038e179@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d4em91gppr7mcf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Instancia o sqlalchemy usando as configurações acima
db: SQLAlchemy
# CADASTROS 

@app.route("/cadastrar/autonomo", methods=['POST'])
def cadastrar_autonomo():
    data = request.get_json()
    try:
        nome = str(data['nome'] )
        email = str(data['email'])
        senha = str(data['senha'] )
        datanasc =  str(data['datanasc'])
        cpf = str(data['cpf'])
        tel = str(data['tel'] )
        foto = bytes([data['foto']])
        plano = data['plano'] 
        categoria = str(data['categoria'] )
        preco = data['preco'] 
        pedidos = data['pedidos'] 
        descricao = str(data['descricao'] )
        avaliacao = data['avaliacao']
        query = f"INSERT INTO autonomo VALUES (NULL, '" + str(nome) + "', '" + str(email) + "', '" + str(senha) + "', " + str(datanasc) + ", '" + str(cpf) + "', '" + str(tel) + "', " + str(foto) + "," + str(plano) + ", '" + str(categoria) + "', " + str(preco) + ", " + str(pedidos) + ", '" + str(descricao) + "'," + str(avaliacao) + ")" 
        db.session.execute(query)
        db.commit()
    except Exception as erro:
        print(erro)
        response = {"mensagem": "nao foi possivel cadastrar autonomo"}
    
    else:
        response = {"mensagem": "autonomo cadastrado com sucesso"}

    return jsonify(response)

# @app.route("/cadastrar/cliente", methods=['POST'])
# def cadastrar_cliente():
#     data = request.get_json()
    
#     response = dbCliente.cadastrar_cliente(nome=data['nome'],email=data['email'], 
#                                             senha=data['senha'],datanasc=data['datanasc'],
#                                             cpf=data['cpf'],tel=data['tel'],
#                                             foto=data['foto'])
                                            
#     return jsonify(response)

# # LOGIN

# @app.route("/login/autonomo", methods=['POST'])
# def login_autonomo():
#     data = request.get_json()
#     response = dbAutonomo.login(email=data['email'], senha=data['senha'])
#     return jsonify(response)

# @app.route("/login/cliente", methods=['POST'])
# def login_cliente():
#     data = request.get_json()
#     response = dbCliente.login(email=data['email'], senha=data['senha'])
#     return jsonify(response)

# # EDITAR

# @app.route("/editar/autonomo", methods=['POST'])
# def editar_autonomo():
#     data = request.get_json()
#     response = dbAutonomo.editar_autonomo(id=data['id'],nome=data['nome'],email=data['email'], 
#                                             senha=data['senha'], tel=data['tel'],
#                                             foto=data['foto'], preco=data['preco'],
#                                             descricao=data['descricao'], categoria=data['categoria'], datanasc=data['datanasc'])
#     return jsonify(response)

# @app.route("/editar/cliente", methods=['POST'])
# def editar_cliente():
#     data = request.get_json()
#     response = dbCliente.editar_cliente(id=data['id'],nome=data['nome'],email=data['email'], 
#                                         senha=data['senha'], datanasc=data['datanasc'], tel=data['tel'], foto=data['foto'])
                                            
#     return jsonify(response)

# # DELETAR

# @app.route("/deletar/autonomo",methods=['DELETE'])
# def deletar_autonomo():
#     data = request.get_json()
#     response = dbAutonomo.excluir_autonomo(data['id'])
#     return jsonify(response)

# @app.route("/deletar/cliente",methods=['DELETE'])
# def deletar_cliente():
#     data = request.get_json()
#     response = dbCliente.excluir_cliente(data['id'])
#     return jsonify(response)

# # VISUALIZAR

# @app.route("/ver/autonomo",methods=['POST'])
# def ver_autonomo():
#     data = request.get_json()
#     response = dbAutonomo.mostrar_autonomo_individual(data['id'])
#     return jsonify(response)

# @app.route("/ver/cliente",methods=['POST'])
# def ver_cliente():
#     data = request.get_json()
#     response = dbCliente.mostrar_cliente_individual(data['id'])
#     return jsonify(response)

# # VISUALIZAR - TODOS AUTONOMOS

# @app.route("/ver/todos", methods=['GET'])
# def ver_todos():
#     response = dbAutonomo.mostrar_todos_autonomos()
#     return jsonify(response)

# @app.route("/avaliacao/adicionar", methods=['POST'])
# def adicionar_avaliacao():
#     data = request.get_json()
#     response = dbAutonomo.adicionar_feedback(id=data['id'],nota=data['nota'])
#     return jsonify(response)

# # PORTFOLIO

# @app.route("/portfolio/contar", methods=['POST'])
# def portfolio_contar():
#     data = request.get_json()
#     response = dbAutonomo.contar_imagens_portfolio(data['id'])
#     return jsonify(response)

# @app.route("/portfolio/ver", methods=['POST'])
# def portfolio_ver():
#     data = request.get_json()
#     response = dbAutonomo.mostrar_todas_fotos(data['id'])
    
#     return jsonify(response)

# @app.route("/portfolio/adicionar", methods=['POST'])
# def portfolio_adicionar():
#     data = request.get_json()
#     response = dbAutonomo.adicionar_portfolio(id=data['id'], foto=data['foto'])
#     return jsonify(response)

# @app.route("/portfolio/deletar", methods=['DELETE'])
# def portfolio_deletar():
#     data = request.get_json()
#     response = dbAutonomo.deletar_portfolio(id=data['id'], foto=data['foto'])
#     return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
