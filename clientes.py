import sqlite3

class ClienteBICCO():
    def __init__(self, path) -> None:
        self.db = path

    def cadastrar_cliente(self, nome, email, senha, datanasc, cpf, tel):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO cliente ('Nome','email','senha','DataNasc','CPF','telefone') VALUES ('{nome}', '{email}', '{senha}', '{datanasc}', '{cpf}', '{tel}')" 
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "nao foi possivel cadastrar cliente"}
            
        else:
            return {"mensagem": "cliente cadastrado com sucesso"}
    
    def editar_cliente(self, id, nome, email, senha, tel):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"UPDATE cliente SET 'Nome' = '{nome}','email' = '{email}','senha' = '{senha}','telefone' = '{tel}' WHERE id = {id};" 
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "nao foi possivel alterar dados do cliente"}            
        else:
            return {"mensagem": "dados do cliente alterados com sucesso"}
            
      
    def mostrar_cliente_individual(self, id):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT * FROM cliente WHERE id = {id};'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        return {
                            "acesso": True,
                            "id": linha[0],
                            "nome": linha[1],
                            "email": linha[2],
                            "senha": linha[3],
                            "dataNasc": linha[4],
                            "cpf": linha[5],
                            "tel": linha[6],
                            "foto": linha[7],
                            "plano": linha[8],
                        }
            else:
                return {
                    "acesso": False,
                    "id": None,
                    "nome": None,
                    "email": None,
                    "senha": None,
                    "dataNasc": None,
                    "cpf": None,
                    "tel": None,
                    "foto": None,
                    "plano": None,
                }
                
    
    def login(self, email, senha):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT id, Email, Senha FROM cliente WHERE Email = "{email}" AND Senha = "{senha}";'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        return {"acesso": True, "email": f"{linha[1]}", "senha": f"{linha[2]}", "ID": linha[0]}
                        
            else:
                return {"acesso": False, "email": "", "senha": "", "ID": 0}

    def excluir_cliente(self, id):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f'DELETE FROM Cliente WHERE id = {id}'
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "Não foi possivel exluir cliente"}
            
        
        else:
            return {"mensagem": "cliente excluido com sucesso"}
            

    
