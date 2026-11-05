from services.usuarios import (
    listar_usuarios,
    consultar_usuario_por_id,
    pesquisar_usuarios,
    alterar_usuario,
    excluir_usuario,
)


def tela_cadastro():
    print("\n=== CADASTRO DE USUÁRIO ===")
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")
    return nome, login, senha


def exibir_usuarios(usuarios):
    if not usuarios:
        print("\nNenhum usuário encontrado.")
        return

    print("\n{:<5} {:<30} {:<20}".format("ID", "NOME", "LOGIN"))
    print("-" * 57)

    for usuario in usuarios:
        print("{:<5} {:<30} {:<20}".format(
            usuario["id"],
            usuario["nome"][:30],
            usuario["login"][:20]
        ))


def tela_consultar_usuarios():
    while True:
        print("\n=== CONSULTAR USUÁRIOS ===")
        print("1 - Listar todos")
        print("2 - Consultar por ID")
        print("3 - Pesquisar por nome ou login")
        print("0 - Voltar")

        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            exibir_usuarios(listar_usuarios())

        elif opcao == "2":
            try:
                usuario_id = int(input("Informe o ID: "))
                usuario = consultar_usuario_por_id(usuario_id)
                exibir_usuarios([usuario] if usuario else [])
            except ValueError:
                print("\nInforme um ID numérico válido.")

        elif opcao == "3":
            termo = input("Digite o nome ou login: ").strip()
            if termo:
                exibir_usuarios(pesquisar_usuarios(termo))
            else:
                print("\nInforme um termo para a pesquisa.")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


def tela_alterar_usuario():
    print("\n=== ALTERAR USUÁRIO ===")

    try:
        usuario_id = int(input("ID do usuário: "))
    except ValueError:
        print("\nInforme um ID numérico válido.")
        return

    print("Deixe o campo vazio para manter o dado atual.")
    novo_nome = input("Novo nome: ")
    novo_login = input("Novo login: ")
    nova_senha = input("Nova senha: ")

    alterar_usuario(usuario_id, novo_nome, novo_login, nova_senha)


def tela_excluir_usuario():
    print("\n=== EXCLUIR USUÁRIO ===")

    try:
        usuario_id = int(input("ID do usuário: "))
    except ValueError:
        print("\nInforme um ID numérico válido.")
        return

    confirmacao = input(
        f"Confirma a exclusão do usuário de ID {usuario_id}? (S/N): "
    ).strip().upper()

    if confirmacao == "S":
        excluir_usuario(usuario_id)
    else:
        print("\nExclusão cancelada. Nenhum dado foi removido.")
