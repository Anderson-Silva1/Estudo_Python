"""
    Python permite que o bloco relativo ao except só seja executado caso a exceção levantada seja de determinado tipo. Para isso, o except precisa trazer o tipo de exceção que se deseja capturar.

    -=- Basicamente, o que conseguimos fazer usando o 'except' é definir o tipo de error para rodar um determinado bloco de código -=-
"""

# SEGUE EXEMPLO:

try:
    num = eval(input('Digite um valor: '))
except NameError: # Aqui estamos especificando o tipo do erro
    print('Use valores numéricos...')


"""
    Captura de exceções de múltiplos tipos:
"""

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")