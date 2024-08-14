""" O método .format() em Python é uma maneira poderosa e flexível de formatar strings. 
    Ele permite que você insira valores em uma string de maneira organizada, substituindo os marcadores {} pelos valores fornecidos. 

    SINTAXE:
        "texto {}".format(valor)
            - Onde o "valor" vai para dentro dos parênteses da string anterior
"""

#-------------------------------------------------------------

nome = "Anderson"
idade = 19
altura = 1.65

formatString = "Nome: {}, idade: {}, altura: {}".format(nome, idade, altura)
"""
    "nome" esta indo para a primeira "chave"
    "idade" esta indo para a segunda "chave"
    "altura" esta indo para a terceira "chave"
"""
print(formatString)
#-------------------------------------------------------------
print("")
#-------------------------------------------------------------

# Podemos usar por índices também:

nome = "Anderson"
idade = 19
gosta = "Programar"
                                                                                    # INDICES     0     1     2
formatString = "Ola, meu nome e {0}, tenho {1} anos de idade... e eu ({0}) gosto de {2}".format(nome, idade, gosta)

print(formatString)

#-------------------------------------------------------------
print("")
#-------------------------------------------------------------

# Usando nomes das variáveis:

formatString = "Ola, meu nome e {nome} e tenho {idade} anos de idade".format(nome = "Anderson", idade = 19)
print(formatString)

#-------------------------------------------------------------