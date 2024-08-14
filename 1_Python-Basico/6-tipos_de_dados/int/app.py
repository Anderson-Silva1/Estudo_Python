"""
    INT - É o tipo usado para manipular números inteiros. 
    Fazendo uma analogia com a Matemática, o tipo int é usado
    para elementos do conjunto dos inteiros (Z).
    Números Inteiros que não contém vírgula: 1, 2, 3, 4, 5, 6, 7, 8, 9... 
"""
c_exNumberInt = 10
print(type(c_exNumberInt)) # <class 'int'>

# OBS: Podemos definir MILHAR usando o "_" dentro no number, ex:
c_exNumberIntMilhar = 1_000_000_000 # Usamos isso apenas para deixarmais organizado
print(type(c_exNumberIntMilhar)) # <class 'int'>

#------------------------------------------

# Tranformando outros tipos de dados em "int":
    # Para isso podemos chamar a expressão: int() para fazer a "conversão de tipo" ou "coerção de tipo":

testeString = "123"

print(f"""Estamos pegando uma string:
            {testeString, type(testeString)}

E transformando em Int:
            {int(testeString), type(int(testeString))}""")

#------------------------------------------