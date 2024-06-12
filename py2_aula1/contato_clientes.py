import questionary
import rich
from database_operacoes import conectar, definir_banco_dados, setup
from rich.table import Table

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
        contatos = {
            "id": registro[4],
            "tipo": registro[2],
            "valor": registro[3],
            "contato":{
                "id_cliente": registro[1],
                "nome": registro[0]
            }
        }

    return contatos


def listar_todos_contatos_clientes():
    contatos = consultar_tabela_contatos
    # Veriifcar se a lista de produtos é vazia
    if len(contatos) == 0:
        # Apresentar mensagem de que não existe produto cadastrada
        print("Nenhuma produto cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Forma de Contato")
    tabela.add_column("Valor")

    for contato in contatos:
        tabela.add_row(
            str(contato.get("id")), 
            contato.get("categoria", {}).get("nome"), 
            contato.get("nome"),
        )
    
    console = Console()
    console.print(tabela)


def menu_contatos():
    opcao = 0
    opcoes = [    
        questionary.Choice("Listar todos", 1),
        questionary.Choice("Cadastro", 2),
        questionary.Choice("Editar", 3),
        questionary.Choice("Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu de categoria:", opcoes).ask())
        if opcao == 1:
            listar_todos_contatos_clientes()
        elif opcao == 2:
            cadastrar_contato()
        elif opcao == 3:
            editar_contato()
        elif opcao == 4:
            apagar_contato()


setup()
criar_tabela_contatos()
popular_registro_contatos()
consultar_tabela_contatos()
listar_todos_contatos_clientes()