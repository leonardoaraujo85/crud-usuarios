import mysql.connector
from mysql.connector import Error


def conectar():
    """Estabelece e retorna uma conexão com o banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="sistema_usuarios"
        )

        if conexao.is_connected():
            return conexao

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")

    return None
