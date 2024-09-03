# denominador = 0
# resultado = 10 / denominador
# print(resultado)

# ERROR >> ZeroDivisionError

# CORREÇÃO

denominador = 0
if denominador != 0:
    resultado = 10 / denominador
    print(resultado)
else:
    print('Não é possível divisão por zero')