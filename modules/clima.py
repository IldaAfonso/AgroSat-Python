import json

leituras = []

def cadastrar_clima(conexao):

    try:

        id_leitura = int(input("ID leitura: "))
        temperatura = float(input("Temperatura: "))
        umidade = float(input("Umidade: "))
        chuva = float(input("Índice de chuva: "))
        id_prop = int(input("ID propriedade: "))

        if temperatura > 30:
            risco = "ALTO"
        elif temperatura > 25:
            risco = "MEDIO"
        else:
            risco = "BAIXO"

        cursor = conexao.cursor()

        sql = """
        INSERT INTO LEITURAS_CLIMATICAS
        VALUES (:1, :2, :3, :4, :5, SYSDATE, :6)
        """

        cursor.execute(sql, (
            id_leitura,
            temperatura,
            umidade,
            chuva,
            risco,
            id_prop
        ))

        conexao.commit()

        print("Leitura climática cadastrada!")

    except Exception as erro:
        print(f"Erro: {erro}")


def listar_clima(conexao):

    try:

        cursor = conexao.cursor()

        cursor.execute("""
        SELECT * FROM LEITURAS_CLIMATICAS
        """)

        dados = cursor.fetchall()

        for dado in dados:
            print(dado)

    except Exception as erro:
        print(f"Erro: {erro}")


def atualizar_clima(conexao):

    try:

        id_leitura = int(input("ID leitura: "))

        nova_temp = float(input("Nova temperatura: "))
        nova_umidade = float(input("Nova umidade: "))

        cursor = conexao.cursor()

        sql = """
        UPDATE LEITURAS_CLIMATICAS
        SET
            TEMPERATURA = :1,
            UMIDADE = :2
        WHERE ID_LEITURA = :3
        """

        cursor.execute(sql, (
            nova_temp,
            nova_umidade,
            id_leitura
        ))

        conexao.commit()

        print("Dados climáticos atualizados!")

    except Exception as erro:
        print(f"Erro: {erro}")


def excluir_clima(conexao):

    try:

        id_leitura = int(input("ID leitura: "))

        cursor = conexao.cursor()

        sql = """
        DELETE FROM LEITURAS_CLIMATICAS
        WHERE ID_LEITURA = :1
        """

        cursor.execute(sql, (id_leitura,))

        conexao.commit()

        print("Leitura removida!")

    except Exception as erro:
        print(f"Erro: {erro}")