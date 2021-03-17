from flask import Flask, jsonify
from flask.globals import request
from autonomos import AutonomoBICCO
from clientes import ClienteBICCO
import os


pathbd = r'assets\bancopteste.db'
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

@app.route("/deletar/autonomo",methods=['DELETE'])
def deletar_autonomo():
    data = request.get_json()
    response = dbAutonomo.excluir_autonomo(data['id'])
    return jsonify(response)

@app.route("/deletar/cliente",methods=['DELETE'])
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


if __name__ == "__main__":
    dbAutonomo = AutonomoBICCO(path=pathbd)
    dbCliente = ClienteBICCO(path=pathbd)
    # port = int(os.environ.get("PORT", 5000))
    port = 5000
    app.run(host='localhost', port=port,debug=True)


# WEBSERVICES

# /cadastrar/autonomo OK
# /cadastrar/cliente OK

# /login/autonomo OK 
# /login/cliente OK

# /editar/autonomo OK
# /editar/cliente OK

# /deletar/autonomo OK
# /deletar/cliente OK

# /ver/autonomo OK 
# /ver/cliente OK 
# /ver/todos OK

# /avaliacao/adicionar OK

# /portfolio/<int:id>
# /portfolio/<int:id>/adicionar
# /portfolio/<int:id>/editar
# /portfolio/<int:id>/deletar

