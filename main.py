from services.autenticacao import autenticar
from services.usuarios import cadastrar_usuario
from views.menu import menu_inicial, menu_principal
from views.telas_usuarios import (
    tela_cadastro,
    tela_consultar_usuarios,
    tela_alterar_usuario,
    tela_excluir_usuario,
)

def executar():
    while True:
        opcao = menu_inicial()

        if opcao == "1":
            login = input("Login: ").strip()
            senha = input("Senha: ")

            usuario = autenticar(login, senha)

            if usuario:
                print(f"\nBem-vindo(a), {usuario['nome']}!")
                executar_menu_principal(usuario)
            else:
                print("\nLogin ou senha incorretos.")

        elif opcao == "2":
            nome, login, senha = tela_cadastro()
            cadastrar_usuario(nome, login, senha)

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


def executar_menu_principal(usuario_logado):
    while True:
        opcao = menu_principal(usuario_logado["nome"])

        if opcao == "1":
            nome, login, senha = tela_cadastro()
            cadastrar_usuario(nome, login, senha)

        elif opcao == "2":
            tela_consultar_usuarios()

        elif opcao == "3":
            tela_alterar_usuario()

        elif opcao == "4":
            tela_excluir_usuario()

        elif opcao == "0":
            print("\nSaindo da conta...")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    executar()
