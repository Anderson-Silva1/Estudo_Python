"""
    Módulo random >> Este módulo implementa geradores de números pseudoaleatórios para várias distribuições
"""

"""
    random de números inteiros >> Existe uma seleção uniforme a partir de um intervalo.
"""

"""
    random sequênciais >> 
        1. Existe uma seleção uniforme de um elemento aleatório.
        2. Existe uma função para gerar uma permutação aleatória das posições na lista.
        3. Existe uma função para escolher aleatoriamente sem substituição.
"""

"""
    Distribuições de valores reais >>
"""
import random

number_random = random.random()
print(f"Método random.random(): {number_random}")
# Gera um número aleatório entre 0 e 1

# uniform()
numeros_aleatrorios_entre_10_20 = random.uniform(10,20)
print(f"Método random.uniform(a, b): {numeros_aleatrorios_entre_10_20}")
# Gera um número aleatório entre os números de sua configuração

# gauss(mu, sigma)
mu, sigma = 0, 10
numero_aleatorio = random.gauss(mu, sigma)
print(f"Método random.gauss(mu, sigma): {numero_aleatorio}")
# Gera um número aleatório com média "a" e desvio padrão "b" (distribuição normal padrão)

# normalvariate
mu = 0       # Média
sigma = 1    # Desvio padrão
numero_aleatorio = random.normalvariate(mu, sigma)
print(f"Método random.normalvariate(mu, sigma): {numero_aleatorio}")
# Gera um número aleatório com média "a" e desvio padrão "b" (distribuição normal padrão)


"""
    Funções para números inteiros
"""

# randrange()
number = random.randrange(10)
print(f"Método random.randrange(stop): {number}")

# randrange
number = random.randrange(1, 10, 2)
print(f"Método random.randrange(start, stop, [step]): {number}")

# randint
number = random.randint(1, 8)
print(f"Método random.randint(a, b): {number}")


"""
    Funções para sequências
"""

# choice(seq)
lista = ["Anderson", "Rafaela", "Emanoel", "Dayane", "José"]
escolha = random.choice(lista)
print(f"Método random.choice(seq): {escolha}")
# Pega 1 (um) ítem aleatório de uma lista

# shuffle(x[, random])
lista_shuffle = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(lista_shuffle) # Independe de uma variável
print(f"Método random.shuffle(seq): {lista_shuffle}")
# Embaralha uma lista

# sample(pop, k)
lista_sample = ["Anderson", "Rafaela", "Teste1", "Teste2", "Teste3"]
amostra_2_elementos = random.sample(lista_sample, 2)
print(f"Método random.sample(seq): {amostra_2_elementos}")
# Pega 1 (um) ou mais elementos de uma lista conforme configurado...

"""
    DAR UM TEMPO NA PROGRAMAÇÃO E FOCAR NO CULTO DAS CRIANÇAS E NA AULA DA EBD!!!...
"""

"""
    VOLTAR A DAR O GÁS NA PROGRAMAÇÃO!!!! 25/08/2024
"""

