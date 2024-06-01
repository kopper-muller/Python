import os
import datetime
import questionary

def exemplo_notas():
    notas = []

    notas.append(float(questionary.text("digite a primeira nota").ask()))
    notas.append(float(questionary.text("digite a segunda nota").ask()))
    notas.append(float(questionary.text("digite a terceira nota").ask()))

    soma = notas[0] + notas[1] + notas [2]
    media = soma / 3
    limpar_tela()

    print("Nota 01:", notas[0])
    print("Nota 02:", notas[1])
    print("Nota 03:", notas[2])
    print("media: ", media)


def limpar_tela():
    os.system("cls")


def exemplo_carros():
    carros, anos_fabricacao = [], []
    ano_atual = datetime.datetime.today().year
    # Gerar um vetor com os anos que o usuário pode escolher, como ano de fabricacao
    # anos disponiveis = [1980, 1981, 1982, 1983, ..., 2822, 2823, 2824)
    anos_disponiveis = [str(ano) for ano in range(1988, ano_atual + 1)]
    # Input Entradas
    carros.append(questionary.text("Digite o modelo do carro").ask().strip())
    anos_fabricacao.append(int(questionary.select("Escolhaoanodefabricação:", anos_disponiveis).ask()))
    carros.append(questionary.text("Digite o modelo do carro").ask().strip())
    anos_fabricacao.append(int(questionary.select("Escolhaoanodefabricação:", anos_disponiveis).ask()))
    # Processamento
    idades = []
    idades.append(ano_atual - anos_fabricacao(0))
    idades.append(ano_atual - anos_fabricacao(11))
    # Output (saída)
    limpar_tela()
    print ("Modelo:", carros[0], "foi fabricado em:", anos_fabricacao[0], "Idade:", idades[0])
    print ("Modelo:", carros[1], "foi fabricado em:", anos_fabricacao[1], "Idade:", idades[1])


exemplo_carros()