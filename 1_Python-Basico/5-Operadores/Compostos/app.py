"""
    OPERADORES COMPOSTOS:
        # 1 - += (Simbolo usado) - "mais igual" (Nome) - x += 2 (Instrução) - x = x + 2 (Equivalência)
        # 2 - -= (Simbolo usado) - "menos igual" (Nome) - x -= 2 (Instrução) - x = x - 2 (Equivalência)
        # 3 - *= (Simbolo usado) - "vezes igual" (Nome) - x *= 2 (Instrução) - x = x * 2 (Equivalência)
        # 4 - /= (Simbolo usado) - "dividido igual" (Nome) - x /= 2 (Instrução) - x = x / 2 (Equivalência)
        # 5 - %= (Simbolo usado) - "modulo/resto igual" (Nome) - x %= 2 (Instrução) - x = x % 2 (Equivalência)
"""

x1 = 10
print(f"valor de x = {x1}") # 10

x2 = 10
x2 += 2
print(f"Valor de x com 'mais igual'(2) = {x2}") # 12

x3 = 10
x3 -= 2
print(f"Valor de x com 'menos igual'(2) = {x3}") # 8

x4 = 10
x4 *= 2
print(f"Valor de x com 'vezes igual'(2) = {x4}") # 20

x5 = 10
x5 /= 2
print(f"Valor de x com 'dividido igual'(2) = {x5}") # 5.0

x6 = 10
x6 %= 3
print(f"Valor de x com 'Módulo/Resto igual'(3) = {x6}") # 1
