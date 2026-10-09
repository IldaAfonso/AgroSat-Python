def cadastrar_rota(conexao):

    try:
        id_rota = int(input("ID rota: "))
        origem = input("Origem: ")
        destino = input("Destino: ")
        distancia = float(input("Distância KM: "))
        id_caminhao = int(input("ID caminhão: "))

        tempo = distancia / 80

        if distancia > 300:
            risco = "MEDIO"
        else:
            risco = "BAIXO"

        cursor = conexao.cursor()

        sql = """
        INSERT INTO ROTAS
        VALUES (:1, :2, :3, :4, :5, :6, :7)
        """

        cursor.execute(sql, (
            id_rota,
            origem,
            destino,
            distancia,
            tempo,
            risco,
            id_caminhao
        ))

        conexao.commit()

        print("Rota cadastrada!")

    except Exception as erro:
        print(f"Erro: {erro}")