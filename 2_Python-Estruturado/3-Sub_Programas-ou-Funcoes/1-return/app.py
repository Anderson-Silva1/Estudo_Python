# RETURN >> É o retorno que uma função, estrutura de descisão e/ou repetição irá mandar

# A palavra reservada return indica que a função retorna algum valor. Isso implica que o valor retornado seja armazenado em uma variável do programa chamador (como ocorre na linha 8) ou utilizado como parâmetro para outra função.

# EX:
def teste1 (n1 = 1, n2 = 2) :
    soma = n1 + n2

print(teste1()) # None
# Está retornando o valor "none", o que significa que essa função não está retornando NADA

def teste2 (n1 = 1, n2 = 2) :
    soma = n1 + n2
    return soma

print(teste2()) # 3

#---------------------------------------------------------

# Funções que não possuem um RETURN são chamadas de funções de procedimento

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0

func1(x)
func2(x)
print(f'Programa principal - x = {x}') 