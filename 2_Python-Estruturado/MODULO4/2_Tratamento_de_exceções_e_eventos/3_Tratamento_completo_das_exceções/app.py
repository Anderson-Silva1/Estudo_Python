"""
    Além do  try e do except, temos o else e o finally, que são opicionais
"""

# SINTAXE COMPLETA DE TRATAMENTO DE ERROS

# try:
#   Bloco 1
# except Exception1:
#   Bloco tratador para Exception1
# except Exception2:
#   Bloco tratador para Exception1
# ...
# else:
#   Bloco 2 – executado caso nenhuma exceção seja levantada
# finally:
#   Bloco 3 – executado independente do que ocorrer
# Instrução fora do try/except

try:
    number = eval(input('Digite um valor: '))
except NameError:
    print('Use apenas números...')
else: # Será xecultado quando não levantar nenhuma exceção
    print('try executado com sucesso, sem exceções')
finally: # Sempre será execultado, independente do resultado
    print('Exeção tratada com sucesso')