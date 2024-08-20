"""
    STRING >> String também é uma estrutura de dado, pois em Python ela possui índex...
"""

texto = "Junior Soares de Lima"

print(texto[:6]) # Junior
print(texto[7:14]) # Soares
print(texto[14:16]) # de
print(texto[17:]) # Lima

# Como vimos podemnos selecionar partes do nosso texto usando a indexação

# Podemos ver a quantidades de caracteres:
print(len(texto)) # Possui 21 caracteres, contando com os espaçoes em branco


"""
    DENTRO DO STRING >> Ainda temos métodos únicos paratratamentos de dados em String:
        PRINCIPAIS:
            texto.capitalize() >> Transforma todas as primeiras letras de cada palavra em maiúscula
            texto.upper() >> Tranforma todas as letras em maiúsculas
            texto.lower() >> Transforma todas a lestras em minúsculas
            texto.title() >> Transforma em um texto descritivo
            texto.split() >> Transforma em Lista
"""

print(texto.capitalize())
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.split())