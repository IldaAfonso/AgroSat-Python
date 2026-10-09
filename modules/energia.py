def cadastrar_energia(conexao):

    try:

        id_energia = int(input("ID energia: "))
        consumo = float(input("Consumo: "))
        producao = float(input("Produção solar: "))
        id_prop = int(input("ID propriedade: "))

        eficiencia = (producao / consumo) * 100

        cursor = conexao.cursor()

        sql = """
        INSERT INTO ENERGIA
        VALUES (:1, :2, :3, :4, SYSDATE, :5)
        """

        cursor.execute(sql, (
            id_energia,
            consumo,
            producao,
            eficiencia,
            id_prop
        ))

        conexao.commit()

        print("Energia cadastrada!")

    except Exception as erro:
        print(f"Erro: {erro}")


def listar_energia(conexao):

    try:

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM ENERGIA")

        dados = cursor.fetchall()

        for dado in dados:
            print(dado)

    except Exception as erro:
        print(f"Erro: {erro}")


def atualizar_energia(conexao):

    try:

        id_energia = int(input("ID energia: "))
        novo_consumo = float(input("Novo consumo: "))

        cursor = conexao.cursor()

        sql = """
        UPDATE ENERGIA
        SET CONSUMO_KWH = :1
        WHERE ID_ENERGIA = :2
        """

        cursor.execute(sql, (
            novo_consumo,
            id_energia
        ))

        conexao.commit()

        print("Energia atualizada!")

    except Exception as erro:
        print(f"Erro: {erro}")


def excluir_energia(conexao):

    try:

        id_energia = int(input("ID energia: "))

        cursor = conexao.cursor()

        sql = """
        DELETE FROM ENERGIA
        WHERE ID_ENERGIA = :1
        """

        cursor.execute(sql, (id_energia,))

        conexao.commit()

        print("Energia removida!")

    except Exception as erro:
        print(f"Erro: {erro}")