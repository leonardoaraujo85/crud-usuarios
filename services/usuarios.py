from mysql.connector import Error, IntegrityError
from services.conexao import conectar


def cadastrar_usuario(nome, login, senha):
    """Cadastra um usuário após validar os campos e o login."""
    nome = nome.strip()
    login = login.strip()

    if not nome or not login or not senha.strip():
        print("\nPreencha todos os campos obrigatórios.")
        return False

    conexao = conectar()

    if conexao is None:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        # Verifica se o login já está cadastrado.
        cursor.execute(
            "SELECT id FROM usuario WHERE login = %s",
            (login,)
        )

        if cursor.fetchone():
            print("\nEste login já está sendo utilizado.")
            return False

        sql = """
            INSERT INTO usuario (nome, login, senha)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (nome, login, senha))
        conexao.commit()

        print("\nUsuário cadastrado com sucesso!")
        return True

    except IntegrityError:
        # A restrição UNIQUE do banco também impede duplicidade.
        print("\nNão foi possível cadastrar: este login já existe.")
        return False

    except Error as erro:
        print(f"\nErro ao cadastrar usuário: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        conexao.close()


def listar_usuarios():
    """Retorna todos os usuários, sem incluir suas senhas."""
    conexao = conectar()

    if conexao is None:
        return []

    cursor = None

    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, login FROM usuario ORDER BY id")
        return cursor.fetchall()

    except Error as erro:
        print(f"Erro ao listar usuários: {erro}")
        return []

    finally:
        if cursor:
            cursor.close()
        conexao.close()


def consultar_usuario_por_id(usuario_id):
    """Consulta um usuário específico pelo ID."""
    conexao = conectar()

    if conexao is None:
        return None

    cursor = None

    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, nome, login FROM usuario WHERE id = %s",
            (usuario_id,)
        )
        return cursor.fetchone()

    except Error as erro:
        print(f"Erro ao consultar usuário: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        conexao.close()


def pesquisar_usuarios(termo):
    """Pesquisa usuários pelo nome ou login."""
    conexao = conectar()

    if conexao is None:
        return []

    cursor = None

    try:
        cursor = conexao.cursor(dictionary=True)
        sql = """
            SELECT id, nome, login
            FROM usuario
            WHERE nome LIKE %s OR login LIKE %s
            ORDER BY nome
        """
        pesquisa = f"%{termo.strip()}%"
        cursor.execute(sql, (pesquisa, pesquisa))
        return cursor.fetchall()

    except Error as erro:
        print(f"Erro ao pesquisar usuários: {erro}")
        return []

    finally:
        if cursor:
            cursor.close()
        conexao.close()


def alterar_usuario(usuario_id, novo_nome, novo_login, nova_senha):
    """Altera somente os campos informados; campo vazio mantém o valor atual."""
    if not novo_nome.strip() and not novo_login.strip() and not nova_senha.strip():
        print("\nNenhuma alteração foi informada.")
        return False

    conexao = conectar()

    if conexao is None:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT id FROM usuario WHERE id = %s", (usuario_id,))
        if cursor.fetchone() is None:
            print("\nUsuário não encontrado.")
            return False

        if novo_login.strip():
            cursor.execute(
                "SELECT id FROM usuario WHERE login = %s AND id <> %s",
                (novo_login.strip(), usuario_id)
            )
            if cursor.fetchone():
                print("\nEste login já pertence a outro usuário.")
                return False

        campos = []
        valores = []

        if novo_nome.strip():
            campos.append("nome = %s")
            valores.append(novo_nome.strip())

        if novo_login.strip():
            campos.append("login = %s")
            valores.append(novo_login.strip())

        if nova_senha.strip():
            campos.append("senha = %s")
            valores.append(nova_senha)

        valores.append(usuario_id)
        sql = f"UPDATE usuario SET {', '.join(campos)} WHERE id = %s"

        cursor.execute(sql, tuple(valores))
        conexao.commit()

        if cursor.rowcount > 0:
            print("\nUsuário alterado com sucesso!")
        else:
            print("\nNenhum dado foi modificado.")
        return True

    except IntegrityError:
        print("\nNão foi possível alterar: o login já existe.")
        return False

    except Error as erro:
        print(f"\nErro ao alterar usuário: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        conexao.close()


def excluir_usuario(usuario_id):
    """Exclui um usuário pelo ID, após a confirmação feita na tela."""
    conexao = conectar()

    if conexao is None:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuario WHERE id = %s", (usuario_id,))

        if cursor.rowcount == 0:
            print("\nUsuário não encontrado. Nenhum registro foi excluído.")
            return False

        conexao.commit()
        print("\nUsuário excluído com sucesso!")
        return True

    except Error as erro:
        print(f"\nErro ao excluir usuário: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        conexao.close()
