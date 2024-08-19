"""
    SubProgramas em Python >> São blocos de código que realizam tarefas específicas
                              dentro de um programa maior. Eles são fundamentais para
                              a organização e reutilização de código em linguagens de programação.

                                                            NOTE: --"Em Python, chamamos SUBPROGRAMAS de FUNÇÕES."
    
    Características gerais dos subprogramas:
        1 - Ponto único de entrada >> Cada subprograma tem um único ponto de entrada, que é onde sua execução começa.
        2 - Suspenção do programa chamador >> Quando um subprograma é chamado, o programa chamador é suspenso até que o subprograma termine sua execução.
        3 - Retorno ao chamador >> Após a execução do subprograma, o controle sempre retorna ao ponto de chamada no programa chamador.


    Definições básicas de subprogramas:
        1 - Definição de subprograma >> Um subprograma, ou função, é definido quando o desenvolvedor
            especifica nome, parâmetros (se houver) e o conjunto de ações que ele executará. Isso cria
            uma "interface" que descreve como a função deve ser chamada e o que ela faz.
        2 - Chamada de subprograma >> Uma função é chamada quando o programa executa uma instrução que
            solicita explicitamente a execução dessa função. Essa chamada ativa a função, fazendo com que
            o Python execute o bloco de código associado a ela.
        3 - Ativação do subprograma >> Uma vez chamada, a função se torna ativa. Ela continua em execução
            até que todas as instruções dentro dela sejam executadas. Quando a função termina, o controle
            retorna ao ponto de onde a função foi chamada.
        4 - Cabeçalho do subprograma >> O cabeçalho de uma função é a primeira parte da definição da função.
            Ele inclui o nome da função e, opcionalmente, uma lista de parâmetros.

        
        SINTAXE:
            def <nome da função>( <Parâmetro se houver> ):
                <Bloco de código>
                pass
"""

# Primeira Função
def hello_world () : # Assim declaramos uma função 
    print("Hello World") # Conteúdo dessa função

hello_world() # Assim chamamos uma função

# NOTE: Em Python, as sentenças de função "def" são executáveis. Isso implica que a função só pode ser chamada após a execução da sentença def.

#--------------------------------------------------

# EXEMPLO DE UM AFUNÇÃO FUNCIONAL
    # Função onde conseguimos o dobro de um números:

def func_soma (n1, n2) :
    return n1 + n2

print(func_soma(10, 20)) # 30

# ESTAMOS USANDO PARÂMETROS, QUE É O QUE VAMOS PARENDER POSTERIORMENTE...

#--------------------------------------------------
print("")
#--------------------------------------------------

# SUBPROGRAMAS EM PYTHON PODEM SER: 
    # 1 - PROCEDIMENTOS >> São aqueles que não retornam valores
    # 2 - FUNÇÕES >> São aquelas que retornam valores.

# PROCEDIMENTOS
def teste_procedimento (n1 = 1, n2 = 2) :
    soma = n1 + n2
    print(soma)
teste_procedimento() # 3

# FUNÇÕES 
def teste_funcao (n1 = 2, n2 = 3) :
    soma = n1 + n2
    return soma
print(teste_funcao()) # 5

#--------------------------------------------------