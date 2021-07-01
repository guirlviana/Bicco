from flask import Flask, jsonify
from flask.globals import request
from autonomos import AutonomoBICCO
from clientes import ClienteBICCO
import os
import getDataBase

pathbd = getDataBase.get_data_base()
app = Flask(__name__)

# CADASTROS 

@app.route("/cadastrar/autonomo", methods=['POST'])
def cadastrar_autonomo():
    data = request.get_json()
    
    response = dbAutonomo.cadastrar_autonomo(nome=data['nome'],email=data['email'], 
                                            senha=data['senha'],datanasc=data['datanasc'],
                                            cpf=data['cpf'],tel=data['tel'],
                                            foto=data['foto'], plano=data['plano'], 
                                            categoria=data['categoria'],preco=data['preco'],
                                            pedidos=data['pedidos'], descricao=data['descricao'], avaliacao=data['avaliacao'])

    return jsonify(response)

@app.route("/cadastrar/cliente", methods=['POST'])
def cadastrar_cliente():
    data = request.get_json()
    
    response = dbCliente.cadastrar_cliente(nome=data['nome'],email=data['email'], 
                                            senha=data['senha'],datanasc=data['datanasc'],
                                            cpf=data['cpf'],tel=data['tel'],
                                            foto=data['foto'])
                                            
    return jsonify(response)

# LOGIN

@app.route("/login/autonomo", methods=['POST'])
def login_autonomo():
    data = request.get_json()
    response = dbAutonomo.login(email=data['email'], senha=data['senha'])
    return jsonify(response)

@app.route("/login/cliente", methods=['POST'])
def login_cliente():
    data = request.get_json()
    response = dbCliente.login(email=data['email'], senha=data['senha'])
    return jsonify(response)

# EDITAR

@app.route("/editar/autonomo", methods=['POST'])
def editar_autonomo():
    data = request.get_json()
    response = dbAutonomo.editar_autonomo(id=data['id'],nome=data['nome'],email=data['email'], 
                                            senha=data['senha'], tel=data['tel'],
                                            foto=data['foto'], preco=data['preco'],
                                            descricao=data['descricao'], categoria=data['categoria'], datanasc=data['datanasc'])
    return jsonify(response)

@app.route("/editar/cliente", methods=['POST'])
def editar_cliente():
    data = request.get_json()
    response = dbCliente.editar_cliente(id=data['id'],nome=data['nome'],email=data['email'], 
                                        senha=data['senha'], datanasc=data['datanasc'], tel=data['tel'], foto=data['foto'])
                                            
    return jsonify(response)

# DELETAR

@app.route("/deletar/autonomo",methods=['POST'])
def deletar_autonomo():
    data = request.get_json()
    response = dbAutonomo.excluir_autonomo(data['id'])
    return jsonify(response)

@app.route("/deletar/cliente",methods=['POST'])
def deletar_cliente():
    data = request.get_json()
    response = dbCliente.excluir_cliente(data['id'])
    return jsonify(response)

# VISUALIZAR

@app.route("/ver/autonomo",methods=['POST'])
def ver_autonomo():
    data = request.get_json()
    response = dbAutonomo.mostrar_autonomo_individual(data['id'])
    return jsonify(response)

@app.route("/ver/cliente",methods=['POST'])
def ver_cliente():
    data = request.get_json()
    response = dbCliente.mostrar_cliente_individual(data['id'])
    return jsonify(response)

# VISUALIZAR - TODOS AUTONOMOS

@app.route("/ver/todos", methods=['GET'])
def ver_todos():
    response = dbAutonomo.mostrar_todos_autonomos()
    return jsonify(response)

@app.route("/avaliacao/adicionar", methods=['POST'])
def adicionar_avaliacao():
    data = request.get_json()
    response = dbAutonomo.adicionar_feedback(id=data['id'],nota=data['nota'])
    return jsonify(response)

# PORTFOLIO

@app.route("/portfolio/contar", methods=['POST'])
def portfolio_contar():
    data = request.get_json()
    response = dbAutonomo.contar_imagens_portfolio(data['id'])
    return jsonify(response)

@app.route("/portfolio/ver", methods=['POST'])
def portfolio_ver():
    data = request.get_json()
    response = dbAutonomo.mostrar_todas_fotos(data['id'])
    
    return jsonify(response)

@app.route("/portfolio/adicionar", methods=['POST'])
def portfolio_adicionar():
    data = request.get_json()
    response = dbAutonomo.adicionar_portfolio(id=data['id'], foto=data['foto'])
    return jsonify(response)

@app.route("/portfolio/deletar", methods=['POST'])
def portfolio_deletar():
    data = request.get_json()
    response = dbAutonomo.deletar_portfolio(id=data['id'], foto=data['foto'])
    return jsonify(response)

@app.route("/senha/autonomo/definir", methods=['POST'])
def definir_senha_autonomo():
    data = request.get_json()
    response = dbAutonomo.definir_senha(id=data['id'],sequencia=data['sequencia'])
    return jsonify(response)

@app.route("/senha/cliente/definir", methods=['POST'])
def definir_senha_cliente():
    data = request.get_json()
    response = dbCliente.definir_senha(id=data['id'],sequencia=data['sequencia'])
    return jsonify(response)

@app.route("/senha/autonomo/recuperar", methods=['POST'])
def recuperar_senha_autonomo():
    data = request.get_json()
    response = dbAutonomo.recuperar_senha(data['senha'])
    return jsonify(response)

@app.route("/senha/cliente/recuperar", methods=['POST'])
def recuperar_senha_cliente():
    data = request.get_json()
    response = dbCliente.recuperar_senha(data['senha'])
    return jsonify(response)

if __name__ == "__main__":    
    dbAutonomo = AutonomoBICCO(path=pathbd)
    dbCliente = ClienteBICCO(path=pathbd)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
