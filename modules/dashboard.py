def exibir_dashboard(conexao):

    try:

        cursor = conexao.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM USUARIOS
        """)

        total_usuarios = cursor.fetchone()[0]


        cursor.execute("""
        SELECT COUNT(*)
        FROM PROPRIEDADES
        """)

        total_propriedades = cursor.fetchone()[0]


        cursor.execute("""
        SELECT COUNT(*)
        FROM ALERTAS
        """)

        total_alertas = cursor.fetchone()[0]


        cursor.execute("""
        SELECT COUNT(*)
        FROM CAMINHOES
        WHERE STATUS_OPERACAO = 'ATIVO'
        """)

        caminhoes_ativos = cursor.fetchone()[0]


        cursor.execute("""
        SELECT COUNT(*)
        FROM ROTAS
        """)

        total_rotas = cursor.fetchone()[0]


        cursor.execute("""
        SELECT AVG(EFICIENCIA_ENERGETICA)
        FROM ENERGIA
        """)

        eficiencia = cursor.fetchone()[0]

        if eficiencia is None:
            eficiencia = 0


        cursor.execute("""
        SELECT SUM(CONSUMO_KWH)
        FROM ENERGIA
        """)

        consumo_total = cursor.fetchone()[0]

        if consumo_total is None:
            consumo_total = 0


        cursor.execute("""
        SELECT COUNT(*)
        FROM ALERTAS
        WHERE NIVEL_ALERTA = 'ALTO'
        """)

        alertas_altos = cursor.fetchone()[0]

        print("\n")

        print("=" * 60)
        print("          DASHBOARD AGROSAT")
        print("=" * 60)

        print(f"""
            Usuários cadastrados: {total_usuarios}

            Propriedades rurais: {total_propriedades}

            Total de alertas: {total_alertas}

            Alertas de alto risco: {alertas_altos}

            Caminhões ativos: {caminhoes_ativos}

            Rotas logísticas: {total_rotas}

            Consumo energético total: {consumo_total:.2f} kWh

            Eficiência energética média:
            {eficiencia:.2f}%
            """)

        print("=" * 60)

        if alertas_altos > 5:

            print("""
            STATUS GERAL:
            ALTO RISCO OPERACIONAL
            """)

        elif alertas_altos > 2:

            print("""
            STATUS GERAL:
            RISCO MODERADO
            """)

        else:

            print("""
        STATUS GERAL:
        OPERAÇÃO ESTÁVEL
        """)

        print("=" * 60)

    except Exception as erro:


        print(f"""
        Erro ao carregar dashboard:

        {erro}
        """)