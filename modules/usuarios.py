import json

usuarios = []




def cadastrar_usuario(conexao):

    try:

        id_usuario = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        perfil = input("Perfil (ADMIN/GESTOR/OPERADOR): ")

        cursor = conexao.cursor()

        sql = """
        INSERT INTO USUARIOS
        VALUES (:1, :2, :3, :4, :5)
        """

        cursor.execute(sql, (
            id_usuario,
            nome,
            email,
            senha,
            perfil
        ))

        conexao.commit()

        usuario = {
            "id": id_usuario,
            "nome": nome,
            "email": email,
            "perfil": perfil
        }

        usuarios.append(usuario)

        salvar_json()

        print("Usuário cadastrado!")

    except Exception as erro:
        print(f"Erro: {erro}")



# READ


def listar_usuarios(conexao):

    try:

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM USUARIOS")

        dados = cursor.fetchall()

        print("\n===== USUÁRIOS =====")

        for usuario in dados:
            print(usuario)

    except Exception as erro:
        print(f"Erro: {erro}")



import hashlib


def criptografar_senha(senha):

    return hashlib.sha256(
        senha.encode()
    ).hexdigest()


def atualizar_usuario(conexao):

    try:

        id_usuario = int(input("ID do usuário: "))

        nome = input("Novo nome: ")
        email = input("Novo email: ")
        perfil = input("Novo perfil: ")

        cursor = conexao.cursor()

        sql = """
        UPDATE USUARIOS
        SET
            NOME = :1,
            EMAIL = :2,
            PERFIL = :3
        WHERE ID_USUARIO = :4
        """

        cursor.execute(sql, (
            nome,
            email,
            perfil,
            id_usuario
        ))

        conexao.commit()

        print("Usuário atualizado!")

    except Exception as erro:
        print(f"Erro: {erro}")



# DELETE


def excluir_usuario(conexao):

    try:

        id_usuario = int(input("ID do usuário: "))

        cursor = conexao.cursor()

        sql = """
        DELETE FROM USUARIOS
        WHERE ID_USUARIO = :1
        """

        cursor.execute(sql, (id_usuario,))

        conexao.commit()

        print("Usuário excluído!")

    except Exception as erro:
        print(f"Erro: {erro}")



# JSON


def salvar_json():

    with open(
        "data/usuarios.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            usuarios,
            arquivo,
            indent=4,
            ensure_ascii=False
        )