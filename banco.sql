CREATE DATABASE IF NOT EXISTS sistema_usuarios;

USE sistema_usuarios;

CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

INSERT INTO usuario (nome, login, senha)
VALUES ('Administrador de Teste', 'admin', '123');

INSERT INTO usuario (nome, login, senha)
VALUES ('Usuário de Teste', 'usuario', '123');