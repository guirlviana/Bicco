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
                        return {"acesso": "true", "email": f"{linha[1]}", "senha": f"{linha[2]}", "id": linha[0]}
            else:
                return {"acesso": "false", "email": "", "senha": "", "id": 0}

    def cadastrar_autonomo(self, nome, email, senha, datanasc, cpf, tel, foto, plano, categoria, preco, pedidos, descricao, avaliacao):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO autonomo ('Nome','email','senha','DataNasc','CPF','telefone','Foto', 'Plano','categoria','ValorHora', 'Pedidos', 'Descricao','Classificacao') VALUES ('{nome}', '{email}', '{senha}', '{datanasc}', '{cpf}', '{tel}', '{foto}', {plano}, '{categoria}', {preco}, {pedidos}, '{descricao}', {avaliacao})" 
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
            
    
    def editar_autonomo(self, id, nome, email, senha, datanasc, tel, foto, categoria, preco, descricao):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"UPDATE autonomo SET 'Nome' = '{nome}','email' = '{email}','senha' = '{senha}','DataNasc' = '{datanasc}','telefone' = '{tel}', 'Foto' = '{foto}' ,'categoria' = '{categoria}','ValorHora' = {preco}, 'Descricao'= '{descricao}' WHERE id = {id};" 
                cursor.execute(query)
                con.commit()
        except Exception:
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
            

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
                            "avaliacao": user[13]
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
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
            
    def adicionar_portfolio(self, id, foto):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO Portfolio ('id_usuario','Foto') VALUES ({id}, '{foto}');"
                cursor.executescript(query)
                con.commit()
        except Exception:
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
        
    def deletar_portfolio(self, id, foto):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"DELETE FROM portfolio WHERE foto = '{foto}' AND id_usuario = {id};"
                cursor.executescript(query)
                con.commit()
        except Exception:
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
    
    def contar_imagens_portfolio(self, id_usuario):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f"SELECT COUNT(id_usuario) FROM portfolio WHERE id_usuario = {id_usuario};"
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        return {"total": linha[0]}

            else:
                return {"total": None}
    
    def mostrar_todas_fotos(self, id):
        photos = []
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f"SELECT foto FROM portfolio WHERE id_usuario = {id};"
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        photos.append(linha[0])
                return {"fotos": photos}

            else:
                return {"fotos": None}

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
                            "id": linha[0],
                            "nome": linha[1],
                            "email": linha[2],
                            "senha": linha[3],
                            "datanasc": linha[4],
                            "cpf": linha[5],
                            "tel": linha[6],
                            "foto": linha[7],
                            "plano": linha[8],
                            "categoria": linha[9],
                            "preco": linha[10],
                            "pedidos": linha[11],
                            "descricao": linha[12],
                            "avaliacao": linha[13],
                            
                        }
            else:
                return {                    
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
                query = f'DELETE FROM Autonomo WHERE id = {id}; DELETE FROM Classificacao WHERE id_usuario = {id}; ; DELETE FROM Portfolio WHERE id_usuario = {id};'
                cursor.executescript(query)
                con.commit()
        except Exception:
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
    
    def definir_senha(self, id, sequencia):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO RecuperarSenhaAutonomo ('id_usuario', 'sequencianumeral') VALUES ({id}, '{sequencia}');"
                cursor.executescript(query)
                con.commit()
        except Exception:
            return {"mensagem": "error"}
            
        else:
            return {"mensagem": "sucesso"}
    
    def recuperar_senha(self, senha):
        
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT id_usuario FROM RecuperarSenhaAutonomo WHERE sequencianumeral = "{senha}";'
            cursor.executescript(query)
            result = cursor.fetchone()
            print(f"RESULTADO {result}")
            if result != 0:
                return {"id": result}
            else:
                return {"id": 0}
            
        


            
