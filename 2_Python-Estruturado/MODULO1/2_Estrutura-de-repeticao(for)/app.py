"""
    1 - FOR é uma estruturade ou laço de repetição baseada em contagem
    2 - As estruturas de repetição for permitem repetir um bloco de código para cada item de uma sequência.
        SINTAXE:
            for <variável> in <sequência>:
                <Bloco que será repetido para todos os itens da sequência>
            <Instrução fora do for>

    3 - Mas antes de detalharmos o for, vamos conhecer uma função de Python que gera
        uma lista de valores numéricos. Essa lista nos ajudará a entender a repetição
        e deixará mais claro o funcionamento do laço.

        LISTAS DO TIPO RANGE()
            - É um método que cria uma sequência de números inteiros desde formas simples até a mais complexa
            
            RANGER SIMPLES:
                SINTAXE:
                    range(3) >> Envolve apenas um argumento. Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até o limite do parâmetro passado (exclusive). 
                    RESULTADO >> Cria a sequência (0, 1, 2)
            
            RANGER NÃO INICIADOS EM 0:
                SINTAXE:
                    range(2, 7) >> Para que a sequência não comece em 0, pode-se informar o início e o fim como parâmetros. Lembre-se de que o parâmetro fim não entra na lista (exclusive o fim). O padrão é incrementar cada termo em uma unidade.
                    RESULTADO >> Cria a sequência (2, 3, 4, 5, 6)

            RANGER INDICANDO INICIO, FIM E PASSO:
                SINTAXE:
                    ranger(1, 5, 8) >> É possível criar sequências mais complexas indicando, na ordem, os parâmetros de início, fim e passo. O passo é o valor que será incrementado de um termo para o próximo.
                    RESULTADO >> Cria a sequência (2, 5, 8)
"""

# Teste com ranger:

for item in range(10): # Inicia no 0, finaliza no 10, e vai contar de 1 em 1
    print(f'Numero teste 1: {item}') # 1 2 3 4 5 6 7 8 9

print("") # identador

for item in range(10, 20): # Inicia no 10 e finaliza no 20, e vai contar de 1 em 1
    print(f'Numero teste 2: {item}') # 10 11 12 13 14 15 16 17 18 19 20

print("") # identador

for item in range(0, 20, 2): # Inicio no 0, vai até o 20, e vai contar de 2 em 2... 
    print(f'Numero teste 3: {item}') # 0 2 4 6 8 10 12 14 16 18 20

print("")

#----------------------------------------------

# EXEMPLO TABUADA USANDO O MÉTODO RANGE
numero = 5
for i in range(11):
    calc = i * numero
    print("{2} * {1} = {0}".format(calc, i, numero))

#----------------------------------------------
print("")
#----------------------------------------------

# FOR EM UMA STRING
stringFor = "Anderson Teste"
for i in stringFor:
    print(f"Letra: {i}")

#----------------------------------------------
print("")
#----------------------------------------------

# FOR EM UMA LISTA SOMANDO TODOS OS VALORES
numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print(f'A soma de todos os numeros e {soma}')

#----------------------------------------------
print("")