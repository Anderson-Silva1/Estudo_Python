# Subprograma que não possuem um RETURN são chamadas de funções de procedimento

# EXEMPLO DE PROCEDIMENTOS
def proc1(x):
    x = 10
    print(f'Funcao procedimento1 - x = {x}')


def proc2(x):
    x = 20
    print(f'Funcao procedimento2 - x = {x}')


x = 0
proc1(x)
proc2(x)
print(f'Programa principal - x = {x}') 

# Observe que em nenhum desses acima possuem o "return"

# Dentro de um procedimento não conseguimos atribuir ele a uma variável

variavelProcedimento = proc1(x)
print(variavelProcedimento) # None

# EXEMPLO DE FUNÇÕES

def func1(x = 0):
    soma = x + 10
    return soma

def func2(x = 0):
    soma = x + 20
    return soma

x = 0

print(f"O valor dessa funcao (func1) e de: {func1(x)}")
print(f"O valor dessa funcao (func2) e de: {func2(x)}")

# As funções podem ser valores de variáveis

variavelFunc = func1(x)
print(variavelFunc) # 10