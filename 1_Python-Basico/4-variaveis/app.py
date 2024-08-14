# Variável é um espaço na memória que é armazenado para um determinado fim.

# Em Python não existe a nececidade de declarar o tipo de dado dessa variável, por isso é considerada uma linguagem de tipagem dinâmica.

# Em Python, as palavras: "teste", "Teste" e "TESTE" são todas diferentes, pois o Python é Case-Sensitive, ele difere entre letras Maiúsculas e Minúsculas

#--------------------------------------------------------
variavelExemplo_1 = "Teste" # String
variavelExemplo_2 = 1 # Number Int
variavelExemplo_3 = 2.0 # Number Float
variavelExemplo_4 = True # Boolean
variavelExemplo_5 = 5 + 6j # Complex
#--------------------------------------------------------

"""REGRAS DE DECLARAÇÃO DE VARIÁVEL
    1 - Não pode iniciar com um número, mas pode conter números;
    2 - Não pode conter espaços, pontos, acentos e outros simbolos ou caracteres especiais esceto o underline;
    3 - Devem começar com uma letra ou underline "_"
    4 - Deve seguir o padrão camelCase ou snake_case de escrita: exemploVariavelCamelCase, exemplo_variavel_snake_case;
    5 - Não deve conter nomes de palavras reservadas: and, as, assert, break, class, continue, def, del, elif, else, 
        except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try,
        while, with e yield..."""

# Palavras reservadas: São palavras que são usadas na sintaxe de uma linguagem de programação

#--------------------------------------------------------

# Constantes em PYTHON
# No Python não existe constantes como no JavaScript por exemplo, mas podemos declarar essas variáveis da seguinte forma:
c_constanteEmPython = "Exemplo de Constante em Python"
# OU
c_CONSTANTESEMPYTHON = "Exemplo de Constante em Python"

#--------------------------------------------------------

#--------------------------------------------------------

""" O Python possui um tipagem dinâmica, o que significa que não precisamos declarar
    o tipo de dado nossa variável vai receber, mas a fins didáticos e em alguns casos 
    para facilitar na legibilidade do código conseguimos dizer qual o tipo de dado 
    essa variável vai receber, para isso fazemos o seguinte: """

string: str = "Teste"
numberInt: int = 1
numberFloat: float = 1.0
boolean: bool = True
complex: complex = 5 + 5j

""" Podemos colocar ':' depois da declaração e antes do sinal de 'Recebe' e colocar
    o tipo de dado dessa variável: str > String; int > Inteiro; float > Real;
    bool > Boleano; complex > complexo """

#--------------------------------------------------------

#--------------------------------------------------------

# Atribuição Múltipla: Podemos declarar mais de uma variável em uma linha de código, basta usar a vírgula "," :

a, b, c, d = 10, 20, 30, 40
print(a, b, c, d)

"""Nesse caso devemos ter cuidado, pois cada elemento é ligado ao valor que ele está
    recebendo pelo seu mesmo lugar, ex:
        a = 10
        b = 20
        c = 30
        d = 40
        
        Se mudarmos a ordem dos lugares dos valores, mudará também a ordem de recebimento:

Trocando a Ordem:   """

a, b, c, d = 20, 10, 40, 30

""" Nesse caso: 
        a = 20
        b = 10
        c = 40
        d = 30
        
        Totalmente diferente da sequência anterior """

#--------------------------------------------------------


