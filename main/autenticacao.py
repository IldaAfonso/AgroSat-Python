from sessao import usuario_logado
import sessao


def login(conexao):

    try:

        email = input("Email: ")
        senha = input("Senha: ")

        cursor = conexao.cursor()

        sql = """
        SELECT
            ID_USUARIO,
            NOME,
            EMAIL,
            PERFIL
        FROM USUARIOS
        WHERE EMAIL = :1
        AND SENHA = :2
        """

        cursor.execute(sql, (email, senha))

        usuario = cursor.fetchone()

        if usuario:

            sessao.usuario_logado = {
                "id": usuario[0],
                "nome": usuario[1],
                "email": usuario[2],
                "perfil": usuario[3]
            }

            print(f"""
                Login realizado com sucesso!

                Usuário: {usuario[1]}
                Perfil: {usuario[3]}
                """)

            return True

        else:
            print("Email ou senha inválidos!")
            return False

    except Exception as erro:
        print(f"Erro no login: {erro}")
        return False


def logout():

    if sessao.usuario_logado:

        print(f"""
     Logout realizado!

        Até logo, {sessao.usuario_logado['nome']}
        """)

        sessao.usuario_logado = None

    else:
        print("Nenhum usuário logado.")



def verificar_login():

    if sessao.usuario_logado is None:

        print("""
    Acesso negado!
Faça login primeiro.
""")

        return False

    return True



def verificar_admin():

    if not verificar_login():
        return False

    if sessao.usuario_logado["perfil"] != "ADMIN":

        print("""
        Apenas ADMIN pode acessar essa funcionalidade!
        """)

        return False

    return True