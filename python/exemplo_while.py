import os

def exemplo_menu():
    apresentar_menu()
    menu_escolhido = int(input("Digite o menu escolhido: "))
    limpar_tela()

    # enquanto o menu escolhido for diferente de sair(20), repetir
    while menu_escolhido != 20:
        # se o menu escolhido for 1, então executará o exemplo de números
        if menu_escolhido == 1:
            exemplo_numeros()
        # senão se o menu escolhido for 2, então executará o exemplo de supermercado
        elif menu_escolhido == 2:
            exemplo_supermercado()

        apresentar_menu()
        menu_escolhido = int(input("Digite o menu escolhido: "))
        limpar_tela()


def limpar_tela():
    os.system("cls")


def apresentar_menu():
    print("|----------------------------------------------------------------|")
    print("|                         SISTEMA PROWAY                         |")
    print("|----------------------------------------------------------------|")
    print("|  1 - Exemplo números                                           |")
    print("|  2 - Exemplo supermercado                                      |")
    print("| 20 - Sair                                                      |")
    print("|----------------------------------------------------------------|")

def exemplo_numeros():
    print("Exemplo de números")     


def exemplo_supermercado():
    print("Exemplo de supermercado")
3.14159295