# Informações aqui a cima só aparecerão caso não tenha nada dentro da própria Função
def fibo(n):
    '''
        Determina o n-ésimo termo da sequência de Fibonacci ok ok ok

        Teste 123

        E assim funcuiona uma DocString

        Vai explicar o que uma função Faz atravéz do Ultilitário "HELP"
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))

# RESULTADO
"""
    Help on function fibo in module __main__:

fibo(n)
    Determina o n-�simo termo da sequ�ncia de Fibonacci ok ok ok

None
"""