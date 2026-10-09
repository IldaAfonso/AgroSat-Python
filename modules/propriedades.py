import json

propriedades = []

def cadastrar_propriedade(conexao):

    try:
        id_prop = int(input("ID: "))
        nome = input("Nome da propriedade: ")
        localizacao = input("Localização: ")
        cultivo = input("Tipo de cultivo: ")
        area = float(input("Área em hectares: "))
        id_usuario = int(input("ID do usuário: "))

        cursor = conexao.cursor()

        sql = """
        INSERT INTO PROPRIEDADES
        VALUES (:1, :2, :3, :4, :5, :6)
        """

        cursor.execute(sql, (
            id_prop,
            nome,
            localizacao,
            cultivo,
            area,
            id_usuario
        ))

        conexao.commit()

        propriedade = {
            "id": id_prop,
            "nome": nome,
            "localizacao": localizacao,
            "cultivo": cultivo,
            "area": area
        }

        propriedades.append(propriedade)

        salvar_json()

        print("\n✅ Propriedade cadastrada com sucesso!")

    except Exception as erro:
        print(f"\n❌ Erro ao cadastrar: {erro}")


# READ


def listar_propriedades(conexao):

    try:

        cursor = conexao.cursor()

        sql = """
        SELECT
            ID_PROPRIEDADE,
            NOME_PROPRIEDADE,
            LOCALIZACAO,
            TIPO_CULTIVO,
            AREA_HECTARES
        FROM PROPRIEDADES
        """

        cursor.execute(sql)

        dados = cursor.fetchall()

        print("\n========== PROPRIEDADES ==========")

        for item in dados:

            print(f"""
ID: {item[0]}
Nome: {item[1]}
Localização: {item[2]}
Cultivo: {item[3]}
Área: {item[4]} hectares
-----------------------------------
""")

    except Exception as erro:
        print(f"\n❌ Erro ao listar: {erro}")


# UPDATE


def atualizar_propriedade(conexao):

    try:

        id_prop = int(input("Digite o ID da propriedade: "))

        novo_nome = input("Novo nome: ")
        nova_localizacao = input("Nova localização: ")
        novo_cultivo = input("Novo cultivo: ")
        nova_area = float(input("Nova área: "))

        cursor = conexao.cursor()

        sql = """
        UPDATE PROPRIEDADES
        SET
            NOME_PROPRIEDADE = :1,
            LOCALIZACAO = :2,
            TIPO_CULTIVO = :3,
            AREA_HECTARES = :4
        WHERE ID_PROPRIEDADE = :5
        """

        cursor.execute(sql, (
            novo_nome,
            nova_localizacao,
            novo_cultivo,
            nova_area,
            id_prop
        ))

        conexao.commit()

        if cursor.rowcount > 0:
            print("\n✅ Propriedade atualizada com sucesso!")
        else:
            print("\n⚠️ ID não encontrado.")

    except Exception as erro:
        print(f"\n❌ Erro ao atualizar: {erro}")



def excluir_propriedade(conexao):

    try:

        id_prop = int(input("Digite o ID da propriedade: "))

        cursor = conexao.cursor()

        sql = """
        DELETE FROM PROPRIEDADES
        WHERE ID_PROPRIEDADE = :1
        """

        cursor.execute(sql, (id_prop,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("\n✅ Propriedade excluída com sucesso!")
        else:
            print("\n⚠️ Propriedade não encontrada.")

    except Exception as erro:
        print(f"\n❌ Erro ao excluir: {erro}")


def salvar_json():

    try:

        with open(
            "data/propriedades.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                propriedades,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    except Exception as erro:
        print(f"\n❌ Erro ao salvar JSON: {erro}")