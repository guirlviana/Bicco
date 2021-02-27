import sqlite3
# Falta fazer as querys para filtros de busca / codigo para guardar imagens no portfolio
# Falta fazer parte de clientes

class AutonomoBICCO():
    def __init__(self, path) -> None:
        self.db = path

    def cadastrar_autonomo(self, nome, email, senha, datanasc, cpf, tel, plano, categoria, preco, pedidos, descricao, avaliacao):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO autonomo ('Nome','email','senha','DataNasc','CPF','telefone','Plano','categoria','ValorHora', 'Pedidos', 'Descricao','Classificacao') VALUES ('{nome}', '{email}', '{senha}', '{datanasc}', '{cpf}', '{tel}', {plano}, '{categoria}', {preco}, {pedidos}, '{descricao}', {avaliacao})" 
                cursor.execute(query)
                con.commit()
        except Exception:
            print('nao foi possivel cadastrar autonomo')
        else:
            print('autonomo cadastrado com sucesso')
    
    def editar_autonomo(self, id, nome, email, senha, tel, preco, descricao):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"UPDATE autonomo SET 'Nome' = '{nome}','email' = '{email}','senha' = '{senha}','telefone' = '{tel}','ValorHora' = {preco}, 'Descricao'= '{descricao}' WHERE id = {id};" 
                cursor.execute(query)
                con.commit()
        except Exception:
            print('nao foi possivel alterar dados do autonomo')
        else:
            print('dados do autonomo alterados com sucesso')

    def mostrar_todos_autonomos(self):
        result = []
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            for binary in range (1, -1, -1):
                query = f'SELECT * FROM Autonomo WHERE plano = {binary} ORDER BY classificacao DESC;'
                cursor.execute(query)
                result.append(cursor.fetchall())
            print(result)
            
    def adicionar_feedback(self, id, nota):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"INSERT INTO classificacao VALUES ({id}, {nota});UPDATE autonomo set Classificacao = (SELECT avg(nota) FROM classificacao WHERE id_usuario = {id}) WHERE id = {id}; UPDATE autonomo SET Pedidos = (SELECT count({id}) FROM Classificacao WHERE id_usuario = {id})"
                cursor.executescript(query)
                con.commit()
        except Exception as erro:
            print('nao foi possivel cadastrar avaliacao ao perfil do autonomo', erro)
        else:
            print('avaliacao ao perfil do autonomo cadastrada com sucesso')
        
    def mostrar_autonomo_individual(self, id):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT * FROM Autonomo WHERE id = {id};'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        print(linha)
            else:
                print('ID não encontrado')

    def excluir_autonomo(self, id):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f'DELETE FROM Autonomo WHERE id = {id}; DELETE FROM Classificacao WHERE id_usuario = {id};'
                cursor.executescript(query)
                con.commit()
        except Exception:
            print('Não foi possivel exluir autonomo')
        
        else:
            print('Autonomo excluindo com sucesso')


    
# db.cadastrar_autonomo('Thiago','thiaguin21@gmail.com','minecraft','2008-01-15','71777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 1.0)
# db.cadastrar_autonomo('Thiago','thiaguin22@gmail.com','minecraft','2008-01-15','72777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 2.0)
# db.cadastrar_autonomo('Thiago','thiaguin23@gmail.com','minecraft','2008-01-15','73777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 3.0)
# db.cadastrar_autonomo('Thiago','thiaguin24@gmail.com','minecraft','2008-01-15','74777777777','11 77777-7777', 0, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 4.0)
# db.cadastrar_autonomo('Thiago','thiaguin26@gmail.com','minecraft','2008-01-15','76777777777','11 77777-7777', 1, 'editor de video', 34.0, 0, 'edito qualquer tipo de video', 0.0)    