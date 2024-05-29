def exemplo03():
    nome1 = input("Digite o nome do produto: ")
    quantidade1 = int(input("Digite a quantidade: "))
    preco_unitario1 = float(input("Digite o valor: "))
    nome2 = input("Digite o nome do produto 2: ")
    quantidade2 = int(input("Digite a quantidade 2: "))
    preco_unitario2 = float(input("Digite o valor do produto 2: "))

    total_parcial1 = quantidade1 * preco_unitario1
    total_parcial2 = quantidade2 * preco_unitario2

    total = total_parcial2 + total_parcial1 

    forma_pagamento = int(input("Escolha a forma de pagmento:\n 1- À vista\n 2- À prazo\n escolha 1 ou 2:"))
    if forma_pagamento == 1:
        valor_desconto = total*0.05
        valor_final = total - valor_desconto
        print("O valor total é R$", total)
        print("O valor do desconto é R$", valor_desconto)
        print("O valor final é R$", valor_final)
    elif forma_pagamento == 2:
        parcelas = int(input("Digite o número de parcelas:"))
        if parcelas<=10:
            print("O valor final é R$", total)
        else:
            valor_juros = total*0.18
            valor_final = valor_juros + total
            valor_parcelas = valor_final/parcelas
            print("O valor total é R$", total)
            print("O valor dos juros é R$", valor_juros, " divididos em ", parcelas, " vezes")
            print("o valor de cada parcela fica R$", valor_parcelas)
            print("O valor final é R$", valor_final)


def exemplo04():
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    if login == "admin" and senha == "1234":
        print ("Autenticado, seja bem vindo")
    else:
        print("Login e/ou senha inválidos")


def exemplo05():
    nome = input("Digite o nome do produto: ").strip()
    produto_vencido_texto = input("O produto está vencido? [SIM/NÃO]").strip().lower()

    preco_unitario = float(input("Digite o preço unitário: R$")).replace(",", ".").replace("R$", "")
    if produto_vencido_texto == "sim":
        produto_vencido_texto = True
    else:
        produto_vencido_texto = False


def exercício01():
    
    nome = input("Digite seu nome: ").strip()
    
    peso = float(input("Digite seu peso em quilos: ").replace(",", ".").replace("kg",""))
    
    altura = float(input("Digite sua altura em metros: ").replace(",", ".").replace("kg",""))
    
    imc = peso/(altura*altura)
    
    if imc >= 18.5:
        classe = "baixo-peso"
    elif imc>18.5 and imc<=25:
        classe = "peso normal"
    elif imc>25 and imc<=30:
        classe = "sobrepreso"
    else:
        classe = "obesidade"
    
    print(nome, ", seu IMC é ", imc, "classificando-te como", classe)


def exercicio02():
    lado1 = float(input("Digite o valor do lado 1 do triângulo: "))
    lado2 = float(input("Digite o valor do lado 2 do triângulo: "))
    lado3 = float(input("Digite o valor do lado 3 do triângulo: "))
    if lado1==lado2 and lado2==lado3:
        print("Este é um triângulo equilátero")
    elif ((lado1==lado2 and lado2!=lado3) or (lado1==lado3 and lado2!=lado3)) or (lado2==lado3 and lado3!=lado1): 
        print("Este é um triângulo isóceles")
    elif (lado1!=lado2 and lado1!=lado3) and (lado3!=lado2):
        print("este é um triângulo escaleno")
    

def exercicio03():
    nota1 = float(input("Digite o valor da nota 1: "))
    nota2 = float(input("Digite o valor da nota 2: "))
    nota3 = float(input("Digite o valor da nota 3: "))
    media = ((nota1+nota2)+nota3)/3
    if media>=7:
        print("Aprovado com média ", media)
    elif media<7 and media>=5:
        print("Em exame com média ", media)
    else:
        print("Reprovado com média ", media)


def exercicio04():
    caracter = input("Digite uma letra: ")
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        print("é uma vogal")
    elif "1" in caracter or 


exercicio02()

