# TUPLAS - Tuplas são sequências imutáveis, tipicamente usadas para armazenar coleções de itens heterogêneos (tipo diferente). Elas são aplicadas também quando é necessário utilizar uma sequência imutável de dados homogêneos (mesmo tipo). Uma tupla pode ser criada de algumas maneiras, tais como:

# TUPLAS - é uma estrutura de dados usada para armazenar uma coleção ordenada de itens...
# Sintaxe:
c_tupla = (1, 2, 3)
print(c_tupla) # (1, 2, 3)
# Mostra a Tupla em si

print(type(c_tupla)) # <class 'tuple'>
# Mostra qual o tipode dado dessa estrutura de dado

print(len(c_tupla)) # 3
# Mosta a quantidade de íytens que essa tupla tem

#--------------------------------

# As TUPLAS e as LISTAS fazem a mesma coisa, a diferênça é que as TUPLAS não podem ser modificadas depois de sua criação, já as LISTAS podem...

# Uma tupla pode ser criada de algumas maneiras, tais como:

# 1 - Usando um par de parênteses para denotar uma tupla.
c_exTupla1 = (1, 2, 3)
print(c_exTupla1) # (1, 2, 3)

# 2 - Separando os itens por vírgulas.
c_exTupla2 = 1, 2, 3
print(c_exTupla2) # (1, 2, 3)
# OU
c_exTupla2 = (1, 2, 3), (4, 5, 6)
print(c_exTupla2) # ((1, 2, 3), (4, 5, 6))

# 3 - Usando o construtor do tipo tuple.
c_exTupla3 = tuple()
print(c_exTupla3) # ()
# OU
iterable = ("Teste1", "Teste2")
c_exTupla3 = tuple(iterable)
print(c_exTupla3)

# OBS: Note que o uso das vírgulas é o que gera a tupla, e não o uso de parênteses. Os parênteses são opcionais, exceto no caso em que queremos gerar uma tupla vazia.

print("")

# TUPLA X LISTA
c_exLista = [1, 2, 3, 4]
print(c_exLista)
print(type(c_exLista))
print(len(c_exLista))

print("")

c_exTupla = (1, 2, 3, 4)
print(c_exTupla)
print(type(c_exTupla))
print(len(c_exTupla))

print("")

#-----------------------------------------

# INDEXAÇÃO - A indexação será a mesma da LISTA:

# index      0  1  2
c_exTupla = (1, 2, 3)
print(f"Esse e um exemplo de indexacao das tuplas: {c_exTupla}")