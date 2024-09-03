"""
    Importação de funções e módulos:
        - Vamos explorar a importação de funções e módulos em Python! Você aprenderá a importar
          bibliotecas nativas da linguagem e a utilizar funções importadas em seu programa.
          Isso ampliará sua capacidade de desenvolvimento e facilitará a reutilização de código.
"""

"""
    Biblioteca padrão Python >> 
        - Python oferece, em seu núcleo, algumas funções que já utilizamos, como print() e input(), além de classes,
          como int, float e str. Logicamente, o núcleo da linguagem Python disponibiliza muitas outras funções (ou métodos)
          e classes além das citadas. Mas, ainda assim, ele é pequeno, tendo o objetivo de simplificar o uso e ganhar
          eficiência.

        - Para aumentar a disponibilidade de funções, métodos e classes, o desenvolvedor pode usar a biblioteca padrão Python.
          Neste material, apresentaremos alguns dos principais recursos dessa biblioteca e a forma de utilizá-los.


        -   A biblioteca padrão Python (Python Standard Library) consiste em milhares de funções, métodos e classes relacionados a determinada finalidade e organizados em componentes chamados de módulos. Há mais de 200 módulos que dão suporte, entre outras coisas, a:
            1 - Operações matemáticas
            2 - Interfaces gráficas com o usuário (GUI)
            3 - Funções matemáticas e geração de números pseudoaleatórios.
"""

"""
    Como usar uma função de módulo importado >> Para usar as funções e os métodos de um módulo, são necessários dois passos. Acompanhe!:
        1 - Fazer a importação do módulo desejado com a instrução:
            EX: import nome_modulo
        2 - Chamar a função desejada, precedida do nome do módulo, com a instrução:
            EX: nome_modulo.nome_funcao(paramêtros)

    - Como exemplo, vamos importar o módulo math (dedicado a operações matemáticas) e calcular a raiz quadrada de 49 por meio da função sqrt()
"""
import math
raiz = math.sqrt(49)
print(raiz) # A ra´z quadrada de 49 é = 7.0

"""
    A partir desse ponto, serão apresentados os principais aspectos dos módulos a seguir:
        NOTE: 1 - math >> Usado para operações matemáticas.
        NOTE: 2 - random >> Usado para gerar números pseudoaleatórios.
        NOTE: 3 - smtplib >> Usado para permitir envio de e-mails.
        NOTE: 4 - time >> Usado para implementar contadores temporais.
        NOTE: 5 - tkinter >> Usado para desenvolver interfaces gráficas.
"""

"""
    Cálculando uma função de 2° grpal
"""

def bascara(a, b, c):
    
    delta = (b**2)-(4*a*c)
    raiz_delta = math.sqrt(delta)
    print(raiz_delta)

    positivo = (-b + delta) / 2*a
    negativo = (-b - delta) / 2*a
    print(f"Valores:\nA = {a}\nB = {b}\nC = {c}")
    print(f"Resultados:\nX = {positivo} & {negativo}")

a, b, c = 2, 5, 13

bascara(a, b, c)