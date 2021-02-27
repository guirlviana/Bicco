import sqlite3
class FiltrosBICCO():
    def __init__(self, path) -> None:
        self.db = path
    

    def filtrar_nome(self, busca):
        try:
            result = []
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                for binary in range (1, -1, -1):
                    query = f"SELECT * FROM Autonomo WHERE Nome LIKE '%{busca}%' AND plano = {binary} ORDER BY classificacao DESC;"
                    cursor.execute(query)
                    result.append(cursor.fetchall())
                
        except Exception:
            print('Não foi possivel filtrar por Categoria')
        
        else:
            print(result)

    def filtrar_categoria(self, busca):
        try:
            result = []
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                for binary in range (1, -1, -1):
                    query = f"SELECT * FROM Autonomo WHERE categoria LIKE '%{busca}%' AND plano = {binary} ORDER BY classificacao DESC;"
                    cursor.execute(query)
                    result.append(cursor.fetchall())
                
        except Exception:
            print('Não foi possivel filtrar por Categoria')
        
        else:
            print(result)
        
    def filtrar_vlhora(self, min, max):
        try:
            result = []
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                for binary in range (1, -1, -1):
                    query = f' SELECT * FROM Autonomo WHERE ValorHora BETWEEN {min} AND {max} AND plano = {binary} ORDER BY classificacao DESC;'
                    cursor.execute(query)
                    result.append(cursor.fetchall())
                
        except Exception:
            print('Não foi possivel filtrar por ')
        
        else:
            print(result)
        
    def filtrar_classificacao(self):
        try:
            result = []
            with sqlite3.connect(self.db, check_same_thread=False) as con:
                cursor = con.cursor()
                for binary in range (1, -1, -1):
                    query = f'SELECT * FROM Autonomo WHERE plano = {binary} ORDER BY classificacao DESC;'
                    cursor.execute(query)
                    result.append(cursor.fetchall())
                
        except Exception:
            print('Não foi possivel filtrar por ')
        
        else:
            print(result)
        