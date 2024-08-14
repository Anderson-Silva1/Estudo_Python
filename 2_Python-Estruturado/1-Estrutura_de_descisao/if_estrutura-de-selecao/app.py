""" 
    Em Python, usamos o IF para executar um bloco de código SE uma condição for verdadeira.

    IF é uma estrutura de seleção ou estrutura descisão onde um bloco de
    código (baseado no resultado da condição) será execultada ou não...
    Se a condição do IF for "TRUE" ele vai execultar o seu bloco de código
    caso seja "FALSE" ele não vai execultar o bloco de código e vai continuar...

        SINTAXE:
            if <condição> :
                <bloco de código>

    Dentro do IF pode contér também o ELSE, ele por sua vêz vai ser execultado caso o IF não seja execultado
        SINTAXE:
            if <condição> :
                <bloco de código>
            else :
                <bloco de código>

    Dentro do IF podemos ter outro elemento, chamado "ELIF", e ele vai ser basicamente
    um outro IF para continuar a verificação, que fica no meio do IF e do ELSE, onde ele
    só ira ser execultado se o IF tiver a condição "FALSE" e a condição dele (ELIF) for "TRUE"

        SINTAXE:
            if <condição> :
                <bloco de código>
            elif <condição> :
                <bloco de código>
            else :
                <bloco de código>

        OBS: Podemos ter mais de um elif em um mesmo conjunto de código, ex:
            SINTAXE:
                if <condição> :
                <bloco de código>
                elif <condição> :
                    <bloco de código>
                elif <condição> :
                    <bloco de código>
                elif <condição> :
                    <bloco de código>
                elif <condição> :
                    <bloco de código>
                else :
                    <bloco de código>
"""

# Exemplo Prático

idade = -2

if idade < 18 :
    print("Voce nao pode dirigir")
elif idade == 18 :
    print("Voce pode tirara sua carteira de habilitacao")
elif idade > 18 :
    print("Voce pode dirigir")
else:
    print("Impossível saber")