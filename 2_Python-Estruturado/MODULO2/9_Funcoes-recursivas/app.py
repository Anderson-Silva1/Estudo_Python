"""
    FUNÇÃO RECURSIVA >> Uma função recursiva é aquela que chama a si mesma
"""
def regressiva(x): # Chamada de inicio da Função
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1) # Chamada da função dentro da função

# regressiva(3) # 3, 2, 1, Acabou

#---------------------------------------------------------------------

"""
    Função Recursiva Fatorial >> O fatorial é uma operação matemática que se aplica a números inteiros não negativos. Denotado por "n!", o fatorial de um número "n" é o produto de todos os números inteiros positivos de 1 até "n".


"""

def fatorial1(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial1(n-1)

def fatorial2(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
           fat = fat*x
        return fat
    
# print(fatorial1(5))
# print(fatorial2(5))

# https://brasilescola.uol.com.br/matematica/fatorial.htm

#--------------------------------------------------------------------

"""
    A sequência de Fibonacci >> A sequência de Fibonacci é uma série matemática onde cada número é a soma dos dois números anteriores. Começa com 0 e 1 (ou, às vezes, com 1 e 1, dependendo da definição). A sequência é definida da seguinte maneira: F ( n ) = F ( n - 1 ) + F ( n - 2 )
"""
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
# print(fibo(10))

# https://www.educamaisbrasil.com.br/enem/matematica/sequencia-de-fibonacci?gad_source=1&gclid=EAIaIQobChMIyPOc5qyGiAMVoWJIAB0VsCTkEAAYASAAEgKI8PD_BwE