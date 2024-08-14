""" FLOAT - É o tipo usado para manipular números com parte inteira e parte decimal,
    chamados de números de ponto flutuante. Fazendo uma analogia com a Matemática,
    o tipo float é usado para elementos do conjunto dos reais (R). Números decimais
    onde contém vírgula: 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0 .... 
"""
c_exNumberFloat = 1.5
print(type(c_exNumberFloat)) # <class 'float'>

# OBS: Todas as operações matemáticas que forém feitas com um number FLOAT o resultado será FLOAT

#------------------------------------------

# Tranformando outros tipos de dados em "int":
    # Para isso podemos chamar a expressão: int() para fazer a "conversão de tipo" ou "coerção de tipo":

testeString = "123"

print(f"""Estamos pegando uma string:
            {testeString, type(testeString)}

E transformando em Float:
            {float(testeString), type(float(testeString))}""")

#------------------------------------------
