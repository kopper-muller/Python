import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="admin"
    )
    return conexao

def criar_banco_dados():
    print("criando banco de dados")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE loja_db")
    conexao.commit
    conexao.close()
    #SHOW SCHEMAS;
    print("banco de dados criado")


def definir_banco_dados(cursor):
    #print("Definindo Banco de Dados loja_db")
    cursor.execute("USE loja_db")
    #print("definido banco de dados")
    return cursor


def criar_tabela_categorias():
    print("Criando tabelas categorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
    )""")
    conexao.commit()
    conexao.close()
    print("tabela criada")


def inserir_registro_tabela_categorias():
    print("Criando registro na tabela de categorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO categorias (nome) VALUES ('hatch');")
    conexao.commit()
    conexao.close()
    print("registro criado ")


def criar_tabela_marcas():
    print("Criando tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""CREATE TABLE marcas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL, endereco varchar(200) not null
    )""")
    conexao.commit()
    conexao.close()
    print("tabela criada")

def criar_tabela_clientes():
    print("Criando tabela clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL, CPF varchar(14) not null
    )""")
    conexao.commit()
    conexao.close()
    print("tabela criada")


criar_banco_dados()
criar_tabela_categorias()
inserir_registro_tabela_categorias()
criar_tabela_marcas()
criar_tabela_clientes()