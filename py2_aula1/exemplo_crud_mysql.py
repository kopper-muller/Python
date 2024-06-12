import os

from database_operacoes import apagar_banco_dados, apagar_registro_tabela_categorias, consultar_registros_tabela_categorias, consultar_registros_tabela_clientes, consultar_registros_tabela_marcas, criar_banco_dados, criar_tabela_categorias, criar_tabela_clientes, criar_tabela_marcas, inserir_registro_tabela_categorias, inserir_registro_tabela_clientes, inserir_registro_tabela_marcas


os.system("cls")
apagar_banco_dados()
criar_banco_dados()
criar_tabela_categorias()
inserir_registro_tabela_categorias("Hatch")   
inserir_registro_tabela_categorias("Sedan") 
apagar_registro_tabela_categorias(1)
consultar_registros_tabela_categorias()

criar_tabela_marcas()
inserir_registro_tabela_marcas("Fiat", "SC - Blumenau - Rua São Paulo - 1740")

criar_tabela_clientes()
inserir_registro_tabela_clientes("John Doe", "920.192.381-20")

consultar_registros_tabela_marcas()
consultar_registros_tabela_clientes()



# Ex. Criar um def para criar a tabela de marcas
#       Marcas deve conter os seguintes campos:
#           - id
#           - nome VARCHAR(50)
#           - endereço VARCHAR(150)
# Ex. Criar um def para criar a tabela de clientes
#       Clientes deve conter os seguintes campos:
#           - id
#           - nome VARCHAR(100)
#           - cpf VARCHAR(14)