def cadastrar_caminhao(conexao):

    try:

        id_caminhao = int(input("ID caminhão: "))
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        capacidade = float(input("Capacidade: "))
        status = input("Status: ")

        cursor = conexao.cursor()

        sql = """
        INSERT INTO CAMINHOES
        VALUES (:1, :2, :3, :4, :5)
        """

        cursor.execute(sql, (
            id_caminhao,
            placa,
            modelo,
            capacidade,
            status
        ))

        conexao.commit()

        print("Caminhão cadastrado!")

    except Exception as erro:
        print(f"Erro: {erro}")


def listar_caminhoes(conexao):

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM CAMINHOES")

    dados = cursor.fetchall()

    for dado in dados:
        print(dado)


def atualizar_caminhao(conexao):

    try:

        id_caminhao = int(input("ID caminhão: "))
        novo_status = input("Novo status: ")

        cursor = conexao.cursor()

        sql = """
        UPDATE CAMINHOES
        SET STATUS_OPERACAO = :1
        WHERE ID_CAMINHAO = :2
        """

        cursor.execute(sql, (
            novo_status,
            id_caminhao
        ))

        conexao.commit()

        print("Caminhão atualizado!")

    except Exception as erro:
        print(f"Erro: {erro}")


def excluir_caminhao(conexao):

    try:

        id_caminhao = int(input("ID caminhão: "))

        cursor = conexao.cursor()

        sql = """
        DELETE FROM CAMINHOES
        WHERE ID_CAMINHAO = :1
        """

        cursor.execute(sql, (id_caminhao,))

        conexao.commit()

        print("Caminhão removido!")

    except Exception as erro:
        print(f"Erro: {erro}")