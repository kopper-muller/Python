import os
import questionary
from rich.console import Console
from rich.table import Table

def  exemplo_tabela():
        tabela = Table(show_header=True)
        tabela.add_column("Modelo")
        tabela.add_column("Ano de fabricação")
        tabela.add_column("Preço")
        tabela.add_row("Gol_quadrado", "1990", "R$14.990.90")
        tabela.add_row("Uno com escada", "1981", "R$9.530")

        console = Console()
        console.print(tabela)


def ex01():
    email = []
  
    for indice in range(7):
        response = input("Digite o e-mail:")
        if response is not None:
            email.append(response)
        else:
            email.append("")  # Append an empty string if user closes the prompt without entering anything

    tabela = Table(show_header=True)
    tabela.add_column("número")
    tabela.add_column("email")
    for indice, email_address in enumerate(email):
        tabela.add_row(str(indice), email_address)

    console = Console()
    console.print(tabela)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def ex02():
    pesos, nomes, alturas, imc = [], [], [], []
    indice = 0
    tabela = Table(show_header=True, header_style= "yellow", show_lines= True)
    tabela.add_column("nomes", style="cyan")
    tabela.add_column("IMC", style="cyan")
    tabela.add_column("classficação", style="cyan")
    while indice < 2:
         indice=indice+1
         nomes.append(questionary.text("Qual seu nome:").ask())
         pesos.append(float(questionary.text("Qual seu peso em kg:").ask()))
         alturas.append(float(questionary.text("Qual sua altura em metros:").ask()))

    for indice in range(len(nomes)):
         imc.append(pesos[indice] / (alturas[indice] ** 2))
         imc_arredondado = round(imc[indice], 2)
         classificacao = classificar_imc(imc_arredondado)
         tabela.add_row(str(nomes[indice]), str(imc_arredondado), classificacao)
    
    
    console = Console()
    console.print(tabela)


def exemplo_alunos():
    #criando 4 vetores, um para o nome dos alunos, nota1 dos alunos ....
    nomes, notas1, notas2, notas3 = [], [], [], []
    #solicitar a quantidade de alunos que deseja cadastrar
    quantidade_alunos =int(questionary.text("Digite a quantidade de alunos para cadastro:").ask().strip())
    #solicitar os dados de cada um dos alunos
    for i in range(quantidade_alunos):
        nomes.append(questionary.text("Digite o nome do aluno: ").ask().strip())
        notas1.append(solicitar_nota("Digite a nota 1: "))
        notas2.append(solicitar_nota("Digite a nota 2: "))
        notas3.append(solicitar_nota("Digite a nota 3: "))

    medias = []
    #calcular a média de cada aluno
    for i in range (quantidade_alunos):
        nota1 = notas1[i]
        nota2 = notas2[i]
        nota3 = notas3[i]
        media=(nota1+nota2+nota3)/3
        medias.append(media)

    # Criar a tabela adicionando o cabeçalho
    tabela = Table(show_header = True, show_lines=True)
    tabela.add_column("Aluno")
    tabela.add_column("Nota 1")
    tabela.add_column("Nota 2")
    tabela.add_column("Nota 3")
    tabela.add_column("Média")

    #Adicionar na tabela os dados dos alunos
    for i in range(quantidade_alunos):
        tabela.add_row(
        nomes[i], 
        formatar_nota(notas1[i]),
        formatar_nota(notas2[i]),
        formatar_nota(notas3[i]), 
        formatar_nota(medias[i])
        )

    console = Console ()
    console.print(tabela)

def solicitar_nota(texto: str) -> str:
    nota = float(questionary.text(texto).ask().strip().replace(",","."))

    while nota < 0 or nota > 10:
        print ("nota inválida! Dve se um valor entre 0 e 10.")
        nota = float(questionary.text().ask().strip().replace(",","."))
    return nota

def formatar_nota(nota: float) -> str:
    nota_formatada = format(nota, ".2f").replace(".", ",")
    return nota_formatada


exemplo_alunos()
   
    