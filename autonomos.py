import sqlite3


class AutonomoBICCO():
    def __init__(self, path) -> None:
        self.db = path
    
    def login(self, email, senha):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT id, Email, Senha FROM autonomo WHERE Email = "{email}" AND Senha = "{senha}";'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        return {"acesso": True, "email": f"{linha[1]}", "senha": f"{linha[2]}", "ID": linha[0]}
            else:
                return {"acesso": False, "email": "", "senha": "", "ID": 0}

    def cadastrar_autonomo(self, nome, email, senha, datanasc, cpf, tel, foto, plano, categoria, preco, pedidos, descricao, avaliacao):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO autonomo ('Nome','email','senha','DataNasc','CPF','telefone','Foto', 'Plano','categoria','ValorHora', 'Pedidos', 'Descricao','Classificacao') VALUES ('{nome}', '{email}', '{senha}', '{datanasc}', '{cpf}', '{tel}', {foto}, {plano}, '{categoria}', {preco}, {pedidos}, '{descricao}', {avaliacao})" 
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "nao foi possivel cadastrar autonomo"}
            
        else:
            return {"mensagem": "autonomo cadastrado com sucesso"}
            
    
    def editar_autonomo(self, id, nome, email, senha, datanasc, tel, foto, categoria, preco, descricao):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"UPDATE autonomo SET 'Nome' = '{nome}','email' = '{email}','senha' = '{senha}','DataNasc' = '{datanasc}','telefone' = '{tel}', 'Foto' = {foto} ,'categoria' = '{categoria}','ValorHora' = {preco}, 'Descricao'= '{descricao}' WHERE id = {id};" 
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "nao foi possivel alterar dados do autonomo"}
            
        else:
            return {"mensagem": "dados do autonomo alterados com sucesso"}
            

    def mostrar_todos_autonomos(self):
        result = []
        store_user = []
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            for binary in range (1, -1, -1):
                query = f'SELECT * FROM Autonomo WHERE plano = {binary} ORDER BY classificacao DESC;'
                cursor.execute(query)
                for user in cursor.fetchall():
                        # (1, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 0.0)
                        data = {
                            "id": user[0],
                            "nome": user[1],
                            "email": user[2],
                            "senha": user[3],
                            "dataNasc": user[4],
                            "cpf": user[5],
                            "tel": user[6],
                            "foto": user[7],
                            "plano": user[8],
                            "categoria": user[9],
                            "valorHora": user[10],
                            "pedidos": user[11],
                            "descricao": user[12],
                            "avaliação": user[13]
                        }
                        store_user.append(data.copy())
                result.append(store_user.copy())
                store_user.clear()
            return {"pago": result[0], "gratuito": result[1]}
            
            

    def adicionar_feedback(self, id, nota):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO classificacao VALUES ({id}, {nota});UPDATE autonomo set Classificacao = (SELECT avg(nota) FROM classificacao WHERE id_usuario = {id}) WHERE id = {id}; UPDATE autonomo SET Pedidos = (SELECT count({id}) FROM Classificacao WHERE id_usuario = {id})"
                cursor.executescript(query)
                con.commit()
        except Exception:
            return {"mensagem": "nao foi possivel cadastrar avaliacao ao perfil do autonomo"}
            
        else:
            return {"mensagem": "avaliacao ao perfil do autonomo cadastrada com sucesso"}
            
        
    def mostrar_autonomo_individual(self, id):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT * FROM Autonomo WHERE id = {id};'
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

    def excluir_autonomo(self, id):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f'DELETE FROM Autonomo WHERE id = {id}; DELETE FROM Classificacao WHERE id_usuario = {id};'
                cursor.executescript(query)
                con.commit()
        except Exception:
            return {"mensagem": "nao foi possivel exluir autonomo"}
            
        else:
            return {"mensagem": "autonomo excluindo com sucesso"}
            


    
# db.cadastrar_autonomo('Thiago','thiaguin21@gmail.com','minecraft','2008-01-15','71777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 1.0)
# db.cadastrar_autonomo('Thiago','thiaguin22@gmail.com','minecraft','2008-01-15','72777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 2.0)
# db.cadastrar_autonomo('Thiago','thiaguin23@gmail.com','minecraft','2008-01-15','73777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 3.0)
# db.cadastrar_autonomo('Thiago','thiaguin24@gmail.com','minecraft','2008-01-15','74777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 4.0)
# db.cadastrar_autonomo('Thiago','thiaguin26@gmail.com','minecraft','2008-01-15','76777777777','11 77777-7777', 1, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 0.0)    