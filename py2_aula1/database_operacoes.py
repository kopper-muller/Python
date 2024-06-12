from typing import Any, Dict, List
import mysql.connector

def conectar():
    # Criando a conexão com o servidor do mysql
    conexao = mysql.connector.connect(
        host="127.0.0.1", # localhost ou 127.0.0.1 é a tua máquina
        port=3306,
        user="root",
        password="admin",
    )
    return conexao


def setup():
    apagar_banco_dados()
    if verificar_banco_dados_existe() == False:
        criar_banco_dados()
        criar_tabelas()
        popular_registros()


def criar_tabelas():
    criar_tabela_categorias()
    criar_tabela_clientes()
    criar_tabela_marcas()
    criar_tabela_produtos()
    criar_tabela_contatos()


def popular_registros():
    popular_registros_tabela_categorias()
    popular_registros_tabela_clientes()
    popular_registros_tabela_marcas()
    popular_registros_tabela_produtos()
    popular_registro_contatos()


def popular_registros_tabela_categorias():
    inserir_registro_tabela_categorias("Hatch")
    inserir_registro_tabela_categorias("Sedan")
    inserir_registro_tabela_categorias("Pickup")
    inserir_registro_tabela_categorias("SUV")

def popular_registros_tabela_clientes():
    inserir_registro_tabela_clientes("João", "123.456.789-10")
    inserir_registro_tabela_clientes("Pedro", "293.123.542-20")
    inserir_registro_tabela_clientes("Carlinhos", "382.349.291-20")
    inserir_registro_tabela_clientes("Sonia", "102.124.126-20")


def popular_registros_tabela_marcas():
    inserir_registro_tabela_marcas("Fiat", "SC - Blumenau - Rua Carlos da Silva - 280")
    inserir_registro_tabela_marcas("Ford", "SC - Blumenau - Rua São Paulo - 120")
    inserir_registro_tabela_marcas("VW", "SC - Blumenau - Rua 2 de setembro - 40")
    inserir_registro_tabela_marcas("Honda", "SC - Blumenau - Rua São Pedro - 380")


def verificar_banco_dados_existe() -> bool:
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    # Consultar na tabela onde contém os dados dos bancos dados, verificando se existe o banco de dados
    # com o nome loja_db
    cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'loja_db'")
    # Obter um registro da consulta
    resultado = cursor.fetchone()
    # Verificar que a consulta retornou um registro, ou seja, o banco de dados existe com o nome 'loja_db'
    if resultado is not None:
        # Desta forma, retornando true, pois o banco de dados existe
        return True
    else:
        return False


def criar_banco_dados():
    # print("Criando banco de dados loja_db")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE loja_db")
    conexao.commit()
    conexao.close()
    # SHOW SCHEMAS;
    # print("Banco de dados criado com sucesso")


def apagar_banco_dados():
    # print("Criando banco de dados loja_db")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor.execute("DROP DATABASE IF EXISTS loja_db")
    conexao.commit()
    conexao.close()
    # SHOW SCHEMAS;
    # print("Banco de dados criado com sucesso")


def definir_banco_dados(cursor):
    # print("Definindo banco dados loja_db")
    cursor.execute("USE loja_db")
    # print("Definido banco dados")
    return cursor

    
def criar_tabela_categorias():
    # print("Criando tabela categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("""
                    CREATE TABLE categorias (
                        id INT PRIMARY KEY AUTO_INCREMENT, 
                        nome VARCHAR(100) NOT  NULL
                    )
                   """)
    conexao.commit()
    conexao.close()
    # print("Criado tabela categorias")


def inserir_registro_tabela_categorias(nome):
    # print("Criando registro na tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    # cursor.execute("INSERT INTO categorias (nome) VALUES ('Hatch');")
    # cursor.execute("INSERT INTO categorias (nome) VALUES ('" + nome + "');")
    cursor.execute("INSERT INTO categorias (nome) VALUES (%s);", (nome,))
    conexao.commit()
    conexao.close()
    # SELECT id, nome FROM categorias;
    # print("Registro criado com sucesso")


def consultar_registros_tabela_categorias():
    # print("Consultando registros da tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("SELECT id, nome FROM categorias")
    # Executar a consulta do SELECT buscando todas as categorias
    registros = cursor.fetchall()
    conexao.close()
    # criar a lista de categorias vazia
    categorias = []
    # percorrer cada um dos registros do banco de dados
    for registro in registros:
        # gerar o dicionário (chave, valor) com os dados do registro
        categoria = {
            "id": registro[0],
            "nome": registro[1]
        }
        # adicionar o dicionário(dados da categoria) na lista de categorias
        categorias.append(categoria)
    # a lista de categorias (que contém uma lista de dicionários com os dados das categorias)
    return categorias


def alterar_registro_tabela_categorias(id: int, nome: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Defini o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE categorias SET nome = %s WHERE id = %s", (nome, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()


def criar_tabela_marcas():
    # print("Criando tabela marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                   CREATE TABLE marcas (
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       nome VARCHAR(50) NOT NULL,
                       endereco VARCHAR(150) NOT NULL
                   )
                   """)
    conexao.commit()
    conexao.close()
    # print("Criado tabela marcas")
    
def inserir_registro_tabela_marcas(nome: str, endereco: str):
    # print("Criando registro na tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO marcas (nome, endereco) VALUES (%s, %s)", (nome, endereco))
    conexao.commit()
    conexao.close()
    # print("Registro criado com sucesso")


def consultar_registros_tabela_marcas():
    # print("Consultando registros da tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("SELECT id, nome, endereco FROM marcas")
    registros = cursor.fetchall()
    conexao.close()
    marcas = []
    for registro in registros:
        marca = {
            "id": registro[0],
            "nome": registro[1],
            "endereco": registro[2],
        }
        marcas.append(marca)
    return marcas


def criar_tabela_clientes():
    # print("Criando tabela clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                   CREATE TABLE clientes(
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       nome VARCHAR(100) NOT NULL,
                       cpf VARCHAR(14) NOT NULL
                   )
                   """)
    conexao.commit()
    conexao.close()
    # print("Criado tabela clientes")
    


def inserir_registro_tabela_clientes(nome: str, cpf: str):
    # print("Criando registro na tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
    conexao.commit()
    conexao.close()
    # print("Registro criado com sucesso")


def consultar_registros_tabela_clientes():
    # print("Consultando registros da tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("SELECT id, nome, cpf FROM clientes")
    registros = cursor.fetchall()
    conexao.close()
    clientes = []
    for registro in registros:
        cliente = {
            "id": registro[0],
            "nome": registro[1],
            "cpf": registro[2],
        }
        clientes.append(cliente)
    return clientes


def apagar_registro_tabela_categorias(id: int):
    # print("Apagando registro da tabela de categorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()
    # print(f"Apagado registro da tabela de categorias com id = {id}")

# CRUD (Create, Read, Update, Delete)


def alterar_registro_tabela_marcas(id: int, endereco: str, nome: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Defini o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE marcas SET nome = %s, endereco = %s WHERE id = %s", (nome, endereco, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()



def apagar_registro_tabela_marcas(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM marcas WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def apagar_registro_tabela_produtos(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def criar_tabela_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        CREATE TABLE produtos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100),
            id_categoria INT, -- FK referenciar uma pk de outra tabela
            FOREIGN KEY (id_categoria) REFERENCES categorias(id) -- Chave estrangeira
        );""")
    conexao.commit()
    conexao.close()


def popular_registros_tabela_produtos():
    inserir_registro_tabela_produtos("HB20 Evolution", 1)
    inserir_registro_tabela_produtos("Celta", 1)
    inserir_registro_tabela_produtos("Onix", 2)
    inserir_registro_tabela_produtos("Ranger", 3)
    inserir_registro_tabela_produtos("S10", 3)


def inserir_registro_tabela_produtos(nome: str, id_categoria: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO produtos (nome, id_categoria) VALUES (%s, %s)", (nome, id_categoria))
    conexao.commit()
    conexao.close()

def consultar_registros_tabela_produtos() -> List[Dict[str, Any]]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        SELECT
            produtos.id,
            produtos.nome,
            produtos.id_categoria,
            categorias.nome
        FROM produtos
        INNER JOIN categorias ON (produtos.id_categoria = categorias.id)
    """)
    registros = cursor.fetchall()
    produtos = []
    for registro in registros:
        produto = {
            "id": registro[0],
            "nome": registro[1],
            "categoria": {
                "id": registro[2],
                "nome": registro[3],
            }
        }
        produtos.append(produto)
    return produtos




def alterar_registro_tabela_produtos(produto: Dict[str, Any]):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute(
        "UPDATE produtos SET nome=%s, id_categoria=%s where id = %s",
        (produto.get("nome"), produto.get("categoria", {}).get("id"), produto.get("id")),    
                )
    conexao.commit()
    conexao.close()

def criar_tabela_contatos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            tipo VARCHAR(100) NOT NULL,
            valor VARCHAR(100) NOT NULL,
            id_cliente INT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        )
    """)
    conexao.commit()
    conexao.close()

def popular_registro_contatos():
    inserir_registro_tabela_contatos(1, "E-mail", "cliente1@exemplo.com")
    inserir_registro_tabela_contatos(1, "Instagram", "@cliente_1")
    inserir_registro_tabela_contatos(1, "Celular", "(01) 234567890")
    inserir_registro_tabela_contatos(2, "Celular", "(02) 234567890")
    inserir_registro_tabela_contatos(2, "Instagram", "@cliente_2")
    inserir_registro_tabela_contatos(3, "E-mail", "cliente3@exemplo.com")

def inserir_registro_tabela_contatos(id_cliente: int, tipo: str, valor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO contatos (id_cliente, tipo, valor) VALUES (%s, %s, %s)", (id_cliente, tipo, valor))
    conexao.commit()
    conexao.close()


def consultar_tabela_contatos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        SELECT 
            clientes.nome, 
            contatos.id_cliente, 
            contatos.tipo, 
            contatos.valor,
            contatos.id
        FROM contatos 
        INNER JOIN clientes ON (contatos.id_cliente = clientes.id)
    """)
    registros = cursor.fetchall()
    contatos = []

    for registro in registros:
        contato = {
            "id": registro[4],
            "tipo": registro[2],
            "valor": registro[3],
            "cliente":{
                "id": registro[1],
                "nome": registro[0]
            }
        }
        contatos.append(contato)
    
    return contatos

def alterar_registro_tabela_contatos(id_cliente: int, valor: str, tipo: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Defini o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE categorias SET valor = %s, id_cliente = %s, tipo = %s WHERE id = %s", (valor, id_cliente, tipo, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()


def apagar_registro_tabela_contatos(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM contatos WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()