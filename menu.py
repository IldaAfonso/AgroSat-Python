from main.conexao import conectar
from modules.usuarios import atualizar_usuario, cadastrar_usuario, excluir_usuario, listar_usuarios, usuarios
from modules.propriedades import atualizar_propriedade, cadastrar_propriedade, excluir_propriedade, listar_propriedades, propriedades
from modules.clima import atualizar_clima, cadastrar_clima, clima, excluir_clima, listar_clima
from modules.energia import atualizar_energia, cadastrar_energia, energia, excluir_energia, listar_energia
from modules.caminhoes import atualizar_caminhao, cadastrar_caminhao, caminhoes, excluir_caminhao, listar_caminhoes
from modules.rotas import rotas
from modules.alertas import alertas
from modules.dashboard import exibir_dashboard

conexao = conectar()

import sys

while True:
    print("""
============ AGROSAT ============

1 - Login
2 - Dashboard Administrativo
3 - Usuários
4 - Propriedades
5 - Clima
6 - Energia
7 - Caminhões
8 - Rotas
9 - Alertas
10 - Logout
11 - Sair

=================================
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Login não implementado ainda.")

    elif opcao == "2":
        exibir_dashboard(conexao)

    elif opcao == "3":
        print("""
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Excluir
""")
        sub = input("Escolha: ")
        if sub == "1":
            cadastrar_usuario(conexao)
        elif sub == "2":
            listar_usuarios(conexao)
        elif sub == "3":
            atualizar_usuario(conexao)
        elif sub == "4":
            excluir_usuario(conexao)

    elif opcao == "4":
        print("""
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Excluir
""")
        sub = input("Escolha: ")
        if sub == "1":
            cadastrar_propriedade(conexao)
        elif sub == "2":
            listar_propriedades(conexao)
        elif sub == "3":
            atualizar_propriedade(conexao)
        elif sub == "4":
            excluir_propriedade(conexao)

    elif opcao == "5":
        print("""
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Excluir
""")
        sub = input("Escolha: ")
        if sub == "1":
            cadastrar_clima(conexao)
        elif sub == "2":
            listar_clima(conexao)
        elif sub == "3":
            atualizar_clima(conexao)
        elif sub == "4":
            excluir_clima(conexao)

    elif opcao == "6":
        print("""
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Excluir
""")
        sub = input("Escolha: ")
        if sub == "1":
            cadastrar_energia(conexao)
        elif sub == "2":
            listar_energia(conexao)
        elif sub == "3":
            atualizar_energia(conexao)
        elif sub == "4":
            excluir_energia(conexao)

    elif opcao == "7":
        print("""
1 - Cadastrar
2 - Listar
3 - Atualizar
4 - Excluir
""")
        sub = input("Escolha: ")
        if sub == "1":
            cadastrar_caminhao(conexao)
        elif sub == "2":
            listar_caminhoes(conexao)
        elif sub == "3":
            atualizar_caminhao(conexao)
        elif sub == "4":
            excluir_caminhao(conexao)

    elif opcao == "8":
        # Rotas
        print("Rotas disponíveis:")
        for r in rotas:
            print(r)

    elif opcao == "9":
        # Alertas
        print("Alertas:")
        for a in alertas:
            print(a)

    elif opcao == "10":
        print("Logout efetuado.")

    elif opcao == "11":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")