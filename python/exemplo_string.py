def exemplo_remover_espacos():
    texto = "      Olá mundo! Seja bemvindo sr. Francisco! "
    # texto = texto.lstrip() # remove espaços da esquerda (começo)
    # texto = texto.rstrip() # remove espaços da direita (fim)
    texto = texto.strip() # remove espaços do começo e do fim
    print(repr(texto))


def exemplo_substituir():
    texto = "Olá mundo! Seja bemvindo sr. Francisco!"
    # texto = texto.replace("bemvindo", "bem vindo") # replace substitui o primeiro parâmetro pelo segundo parâmetro
    # texto = texto.replace("sr.", "Sr.")
    texto = texto.replace("bemvindo", "bem vindo").replace("sr.", "Sr.")
    print(texto)


def exemplo_verificar_contem_parte():
    texto = "Olá mundo! Seja bemvindo sr. Francisco!"
    # Verificar se uma string está dentro de outra string
    contem_texto = "Francisco" in texto
    print(texto)
    print("Contém texto 'Francisco': ", contem_texto)


def exemplo_verificar_nao_contem_parte():
    texto = "Olá mundo! Seja bemvindo sr. Francisco!"
    # Verificar se uma string não contém uma string dentro dela
    nao_contem_sobreonome = "Lucas" not in texto
    print(texto)
    print("Não contém texto 'Lucas': ", nao_contem_sobreonome)


def exemplo_obter_tamanho_texto():
    texto = "Olá mundo! Seja bemvindo sr. Francisco!"
    # Descobrir a quantidade de caracteres da string
    comprimento_da_string = len(texto)
    print(repr(texto))
    print("Quantidade de caracteres: ", comprimento_da_string)


def exemplo_transformar_o_texto_para_maiusculo():
    texto = "Olá mundo! Seja bemvindo sr. Francisco!"
    # Transformar o texto para caixa alta
    texto = texto.upper()
    print(texto)
#só ponha um .upper ou .strip após o nome da bvariavel string, tipo nome.strip()
    
    

def exemplo_transformar_o_texto_para_minusculo():
    texto = "Olá mundo! Seja bemvindo sr. Francisco!"
    # Transformar o texto para caixa baixa
    texto = texto.lower()
    print(texto)


def exemplo_primeira_letra_cada_palavra_maiuscula():
    texto = "outro texto aqui!"
    # Transformar a primeira letra de cada palavra em caixa alta
    texto = texto.title()
    print(texto)


def exemplo_primeira_letra_da_primeira_palavra_maiuscula():
    texto = "outro texto aqui!"
    # Transformar a primeira letra da primeira palavra em caixa alta
    texto = texto.capitalize()
    print(texto)


def exemplo_comeca_com_string():
    texto = "olá mundo"
    # verificar se começa com mundo
    comeca_com_mundo = texto.startswith("mundo") 
    print("Texto começa com 'mundo': ", comeca_com_mundo)


def exemplo_termina_com_string():
    texto = "olá mundo"
    # verificar se termina com mundo
    comeca_com_mundo = texto.endswith("mundo") 
    print("Texto começa com 'mundo': ", comeca_com_mundo)


exemplo_comeca_com_string()
