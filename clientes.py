import sqlite3
# Falta fazer as querys para filtros de busca / codigo para guardar imagens no portfolio
# Falta fazer parte de clientes

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
            print('nao foi possivel cadastrar cliente')
        else:
            print('cliente cadastrado com sucesso')
    
    def editar_cliente(self, id, nome, email, senha, tel):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f"UPDATE cliente SET 'Nome' = '{nome}','email' = '{email}','senha' = '{senha}','telefone' = '{tel}' WHERE id = {id};" 
                cursor.execute(query)
                con.commit()
        except Exception:
            print('nao foi possivel alterar dados do cliente')
        else:
            print('dados do cliente alterados com sucesso')


        
    def mostrar_cliente_individual(self, id):
        with sqlite3.connect(self.db, check_same_thread=False) as con:
            cursor = con.cursor()
            query = f'SELECT * FROM cliente WHERE id = {id};'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) != 0:
                for linha in result:
                    if linha:
                        print(linha)
            else:
                print('ID não encontrado')

    def excluir_cliente(self, id):
        try:
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                query = f'DELETE FROM Cliente WHERE id = {id}'
                cursor.execute(query)
                con.commit()
        except Exception:
            print('Não foi possivel exluir cliente')
        
        else:
            print('Cliente excluindo com sucesso')


    
