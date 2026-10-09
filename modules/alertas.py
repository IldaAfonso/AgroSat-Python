def cadastrar_alerta(conexao):

    try:

        id_alerta = int(input("ID alerta: "))
        tipo = input("Tipo alerta: ")
        descricao = input("Descrição: ")
        nivel = input("Nível: ")
        id_prop = int(input("ID propriedade: "))

        cursor = conexao.cursor()

        sql = """
        INSERT INTO ALERTAS
        VALUES (:1, :2, :3, :4, SYSDATE, :5)
        """

        cursor.execute(sql, (
            id_alerta,
            tipo,
            descricao,
            nivel,
            id_prop
        ))

        conexao.commit()

        print("Alerta cadastrado!")

    except Exception as erro:
        print(f"Erro: {erro}")