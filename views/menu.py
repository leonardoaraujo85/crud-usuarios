def menu_inicial():
    print("\n=== SISTEMA DE USUÁRIOS ===")
    print("1 - Entrar")
    print("2 - Criar uma conta")
    print("0 - Encerrar")
    return input("\nOpção: ").strip()


def menu_principal(nome_usuario):
    print(f"\n=== MENU PRINCIPAL | {nome_usuario} ===")
    print("1 - Cadastrar usuário")
    print("2 - Consultar usuários")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair da conta")
    return input("\nOpção: ").strip()
