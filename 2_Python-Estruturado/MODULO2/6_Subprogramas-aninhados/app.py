"""
    Subprogramas aninhados >> Em Python (e na maioria das linguagens funcionais), é permitido aninhar subprogramas.
"""

# OLHAR O CÓDIGO DE EXEMPLO "codigo15.py"

# A função taximetro() tem, dentro de sua definição, a definição de outra função denominada calculaMult(). Na linha 7, a função calculaMult() é chamada, e o seu retorno é armazenado na variável multiplicador.

# Outro exemplo de Funções aninhadas:

def sum(num):
    soma = num + 100
    return soma

def mult(num):
    mult = num * 5
    return mult

def expoente(num):
    expoente = num ** 2
    return expoente

def resultado(num):
    soma = sum(num) # Está chamando a função "sum" que soma 100 (que faz parte do bloco de código da função "sum") ao parâmetro da função resultado e atribuindo a variável soma
    multiplicacao = soma + mult(soma) # Está chamando a função "mult" que multiplica o parâmetro da mesma (que no caso é o resultado da função "sum") por 5 (que faz parte do bloco de código da função "mult") e está atribuindo o valor a variável "multiplicação"
    expoenteResult = multiplicacao + expoente(multiplicacao) # Está chamando a função "expoente" que eleva o parâmetro da mesma (que no caso é o resultado da função "mult") ao quadrado (que faz parte do bloco de código da função "expoente") e está atribuindo o valor a variável "expoenteResult"
    return expoenteResult # está retornando o valor da variável "expoenteResult"


print(resultado(10)) # RESULTADO >> 436260