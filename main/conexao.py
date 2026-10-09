import oracledb

def conectar():
    try:
        conexao = oracledb.connect(
            user="rm568233",
            password="",
            dsn="localhost/XEPDB1"
        )

        print("Conectado ao Oracle com sucesso!")
        return conexao

    except Exception as erro:
        print(f"Erro ao conectar: {erro}")
        return None