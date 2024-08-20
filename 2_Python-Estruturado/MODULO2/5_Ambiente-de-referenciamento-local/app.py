"""
    Variáveis locais >> Quando um subprograma define as próprias variáveis, ele estabelece ambientes
                        de referenciamento local. Essas variáveis são chamadas de variáveis locais,
                        nas quais seu escopo usualmente é o corpo do subprograma.

    TIPOS DE VARIÁVEIS LOCAIS:
        1 - Dinâmica da Pilha >>
            * São vinculadas ao armazenamento no início da execução do subprograma e desvinculadas quando essa execução termina.
            * As variáveis locais dinâmicas da pilha têm diversas vantagens, e a principal delas é a flexibilidade.
            * Suas principais desvantagens são o custo do tempo – para alocar, inicializar (quando necessário) e liberar tais variáveis para cada chamada ao subprograma – e o fato de que os acessos a essas variáveis locais devem ser indiretos, enquanto os acessos às variáveis estáticas podem ser diretos.
        2 - ESTÁTICAS >>
            * São vinculadas a células de memória antes do início da execução de um programa e permanecem vinculadas a essas mesmas células até que a execução do programa termine.
            * Elas são um pouco mais eficientes que as variáveis locais dinâmicas da pilha, já que não é necessário tempo para alocar ou liberar essas variáveis.
            *Sua maior desvantagem é a incapacidade de suportar recursão.

        NOTE: OBS: Todas as variáveis locais em Python são dinâmicas da pilha.
                   As variáveis globais são declaradas em definições de método;
                   além disso, qualquer variável declarada global em um método
                   precisa ser definida fora dele. Caso haja uma atribuição à
                   variável local com o mesmo nome de uma variável global, a global
                   é implicitamente declarada como local.
"""

#---------------------------------------------------------------------------------------------

# Podemos modificar o valor de variáveis "globais" dentro de SubProgramas

"""
    Para isso, seria necessário explicitar, dentro de cada função, que o nome x é referente a ela. Isso pode ser feito com a palavra reservada global. Além de explicitar a referência à variável global, as funções func1(x) e func2(x) não recebem mais os parâmetros de mesmo nome, já que fazem referência à variável global.
"""

def func1():
    global x # Referência a variável Global "x"
    x += 10 # Somando 10 à variável x (Global)
    print(f'Função func1 - x = {x}')


def func2():
    global x # Referência a variável Global "x"
    x += 20 # Somando 20 à variável x (Global)
    print(f'Função func2 - x = {x}')


x = 0
func1() # Essa função vai atribuir 10 a variável x... Tornando de 0 para 10
func2() # Essa função vai atribuir 20 a variável x... Tornando de 10 (resultado da função anterior) para 30
print(f'Programa principal - x = {x}')