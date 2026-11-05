from mysql.connector import Error
from services.conexao import conectar


def autenticar(login, senha):
    """Retorna os dados do usuário quando login e senha forem válidos."""
    conexao = conectar()

    if conexao is None:
        return None

    cursor = None

    try:
        cursor = conexao.cursor(dictionary=True)

        sql = """
            SELECT id, nome, login
            FROM usuario
            WHERE login = %s AND senha = %s
        """
        cursor.execute(sql, (login, senha))

        usuario = cursor.fetchone()
        return usuario

    except Error as erro:
        print(f"Erro durante a autenticação: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        conexao.close()
