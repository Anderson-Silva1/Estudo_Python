"""
    WHILE é uma estruturade descisão que significa "enquanto", ou seja
    enquanto uma condição for "TRUE"(VERDADEIRA), ele vai execultar o
    respectivo bloco de código:
        SINTAXE:
            while <condição> :
                <bloco de código>
    
    Em conjunto com o WHILE possuem algumas palavras chaves para tratar determinados
    tipos de dados, Essas Palavras são:
        1 - BREAK >> Ele vai fazer a parada do nosso WHILE
            SINTAXE:
                while <consição> :
                    <bloco de código>
                    break
"""

#--------------------------------------------------------------------------------
# EXEMPLO DE WHILE:
number = 0
while number < 10:
    number += 1
    print(number)
#--------------------------------------------------------------------------------
print("")
#--------------------------------------------------------------------------------
# EXEMPLO DE WHILE USANDO BREAK
print("Inicio do while")
while True :
    print("loop")
    text = input("Deseja sair do programa? então digite sair: ")
    if text == "sair" :
        print("Saiu do WHILE")
        break
#--------------------------------------------------------------------------------