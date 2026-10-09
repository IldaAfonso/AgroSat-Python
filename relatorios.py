def gerar_relatorio(conexao):

    try:
        cursor = conexao.cursor()

        sql = """
        SELECT
            P.NOME_PROPRIEDADE,
            L.RISCO_CLIMATICO
        FROM PROPRIEDADES P
        INNER JOIN LEITURAS_CLIMATICAS L
        ON P.ID_PROPRIEDADE = L.ID_PROPRIEDADE
        """

        cursor.execute(sql)

        dados = cursor.fetchall()

        with open("data/relatorios.txt", "w", encoding="utf-8") as arquivo:

            arquivo.write("===== RELATÓRIO AGROSAT =====\n\n")

            for item in dados:
                linha = f"Propriedade: {item[0]} | Risco: {item[1]}\n"
                arquivo.write(linha)

        print("Relatório gerado com sucesso!")

    except Exception as erro:
        print(f"Erro: {erro}")