import os
import questionary
import rich

def menu():
    opcao = 0 
    while opcao != 1000:
        opcoes = [

            questionary.Choice("Categoria - Listar todos", 1),
            questionary.Choice("Categoria - Cadastro", 2),
            questionary.Choice("Categoria - Editar ", 3),
            questionary.Choice("Categoria - Apagar", 4),
            questionary.Choice("Sair", 1000),
        ]
        opcao = int(questionary.select("Escolha o menu:", opcoes).ask())
        
        if opcao == 1:
            listar_todos()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            editar()
        elif opcao == 4:
            apagar()
        else:
            pass
            
        
menu()