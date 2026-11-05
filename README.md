# Sistema de Usuários - Python + MySQL

Projeto didático de CRUD pelo terminal, organizado em `services` e `views` (estrurura mínima de arquitetura).

## 1. Preparar o banco de dados

Abra o MySQL Workbench ou o terminal do MySQL e execute o conteúdo de `banco.sql`.

O script cria o banco `sistema_usuarios`, a tabela `usuario` e dois registros para teste.

## 2. Instalar a biblioteca

No terminal, dentro da pasta do projeto:

```bash
pip install mysql-connector-python
```

Esse comando instala o conector que permite ao Python conversar com o MySQL.

## 3. Configurar a conexão

Abra `services/conexao.py` e informe o usuário e a senha do seu MySQL:

```python
user="root",
password="SUA_SENHA_MYSQL",
```

Se o seu MySQL utilizar outra configuração de host, usuário ou porta, ajuste os parâmetros nessa função.

## 4. Executar

```bash
python main.py
```

O comando inicia o sistema pelo menu do terminal.

## 5. Estrutura

```text
crud_usuarios/
├── main.py
├── banco.sql
├── README.md
├── services/
│   ├── conexao.py
│   ├── autenticacao.py
│   └── usuarios.py
└── views/
    ├── menu.py
    └── telas_usuarios.py
```

## 6. O que foi implementado

- Conexão com o MySQL.
- Cadastro com validação de campos e verificação de login duplicado.
- Autenticação por login e senha.
- Listagem sem exibir senhas.
- Consulta por ID.
- Pesquisa por nome ou login.
- Alteração de nome, login e senha.
- Exclusão com confirmação.
- Uso de `commit()` nas operações de modificação.

## 7. Conceitos importantes

- `connect()`: abre a conexão com o banco de dados.
- `cursor()`: cria o objeto utilizado para enviar comandos SQL.
- `execute()`: executa uma instrução SQL.
- `fetchall()`: recupera todos os registros retornados por uma consulta.
- `fetchone()`: recupera apenas um registro.
- `commit()`: confirma e persiste as alterações no banco.
- `close()`: encerra o cursor ou a conexão.

## Observação didática sobre senhas

Para manter o exercício concentrado na integração Python/MySQL, este exemplo armazena e compara as senhas em texto simples. Isso **não deve ser utilizado em sistemas reais**. Em uma aplicação de produção, as senhas devem ser armazenadas com uma função apropriada de hash de senha, como Argon2 ou bcrypt.
