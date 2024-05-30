def ex01():
    indice = 0
    while indice <3:
        nome = input("Nome do jogo: ")
        preco = float(input("Valor do jogo: ").repalce(",", "."))
        indice=indice+1



def ex02():
    nome = input("digite um nome: ")
    while nome.lower() != "fim":
        nome = input("digite um nome: ")


def ex03():
    idade = int(input("digite sua idade: "))
    while idade <= 128:
        idade = int(input("digite uma idade: "))


def ex04():
    import time
    import os
    
    horas = int(input("horas do timer: "))
    minutos = int(input("minutos do timer: "))
    segundos = int(input("segundos do timer: "))
    
    while (horas!= 0 or minutos != 0 or segundos!= 0):
           
        time.sleep(1)
        os.system("cls") 
        segundos = segundos - 1
        if segundos == -1 and minutos>0:
            minutos = minutos-1 
            segundos = 59
        elif segundos == -1 and minutos==0:
            minutos = 59
            segundos = 59
            horas = horas-1

        print(horas, ":", minutos, ":", segundos)
              

def ex05():
    indice= int(input("quantos carros deseja cadastrar: "))
    valor_total = 0
    ano_total = 0
    numero_G = 0
    numero_A = 0
    while indice>0:
        indice = indice-1
        nome = input("Qual o nome do carro:").capitalize()
        valor = float(input("qual o valor do carro: ".replace(",", "").replace("R$","")))
        ano = int(input("Qual o ano do carro: "))
        valor_total = valor_total + valor
        ano_total = ano_total + ano
        comeca_G = nome.startswith("G")
        comeca_A = nome.startswith("A")
        if comeca_G==True:
            numero_G = numero_G+1
        elif comeca_A==True:
            numero_A = numero_A+1
        
    
    media_valor = valor_total/indice
    media_ano = ano_total/indice
    print("a média dos anos de lançamento é: ", media_ano) 
    print("a média de preço é: ", media_valor) 
    print(numero_A, "começam com A")
    print(numero_G, "começam com G")


ex05()

    

ex04()

