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
    cursor.execute("drop database if exists loja_db")
    
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

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[TABELA CATEGORIAS]-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
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


def inserir_registro_tabela_categorias(nome):
    print("Criando registro na tabela de categorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO categorias (nome) VALUES (%s);", (nome,))
    conexao.commit()
    conexao.close()
    print("registro criado ")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[TABELA CLiENTES]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def criar_tabela_clientes():
    print("Criando tabela clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL, cpf varchar(14) not null
    )""")
    conexao.commit()
    conexao.close()
    print("tabela criada")


def inserir_registro_tabela_clientes(nome: str, cpf: str):
    print("Criando registro na tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("insert into clientes (nome, cpf) values (%s, %s)", (nome, cpf))
    conexao.commit()
    conexao.close()
    print("Registro criado com sucesso")


def consultar_registros_tabela_clientes():
    print("consultando registros da tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("select id, nome, cpf from clientes")
    registros = cursor.fetchall()
    conexao.close()
    for registro in registros:
        print (registro)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[TABELA MARCAS]=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
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


def inserir_registro_tabela_marcas(nome: str, endereco: str):
    print("Criando registro na tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("insert into marcas (nome, endereco) values (%s, %s)", (nome, endereco))
    conexao.commit()
    conexao.close()
    print("Registro criado com sucesso")


def consultar_registros_tabela_marcas():
    print("consultando registros da tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("select id, nome, endereco from marcas")
    registros = cursor.fetchall()
    conexao.close()
    for registro in registros:
        print (registro)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=[APAGANDO CLIENTE]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def apagar_registro_categorias_tabela_categorias(id: int):
    print("Apagando registros da tabela de caegorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("Delete from categorias where id = %s", (id,))
    conexao.commit()
    conexao.close()
    print(f"registro de id={id} apagado")

