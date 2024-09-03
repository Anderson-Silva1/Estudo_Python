"""
    MATH >> Este módulo provê acesso a funções matemáticas de argumentos reais. As funções não podem ser usadas com números complexos.
"""

"""
    O QUE O "MATH" PODE FAZER?
"""

import math

# Raiz quadrada (sqrt())
number = 49
raiz = math.sqrt(number)
print("A raíz quadrada de {} é: {}".format(number, raiz))

# Menor inteiro maior ou igual (ceil())
number = 10.4
arredondar_maior_numero = math.ceil(number)
print(f"Arredondando o número {number} para o maior número inteiro: {arredondar_maior_numero}")

# Maior inteiro menor ou igual (floor())
number = 10.5
arredondar_menor_numero = math.floor(number)
print(f"Arredondando o número {number} para o maior número inteiro: {arredondar_menor_numero}")

# Cosseno
number = 420
cosseno = math.cos(number)
print(f"O cosseno de {number} é: {cosseno}")

# Seno
number = 420
seno = math.sin(number)
print(f"O seno de {number} é: {seno}")

# Valor de PI
valor_PI = math.pi
print(f"O valor de PI é: {valor_PI}")

# Logaritmo
number = 10
number_base = 100
logaritmo = math.log(number, number_base)
print(f"O logaritmo de {number} na base {number_base} é: {logaritmo}")

# número de Euler (também conhecido como número "e")
euler = math.e
print(f"O valor do número de Euler é: {euler}")