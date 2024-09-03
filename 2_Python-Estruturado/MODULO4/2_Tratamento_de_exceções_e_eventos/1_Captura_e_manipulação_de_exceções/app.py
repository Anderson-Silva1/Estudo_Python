"""
    CAPITURA E MANIPULAÇÕA DE EXCEÇÕES >> Para evitar que os programas sejam interrompidos quando uma
                                          exceção é levantada, é possível planejar um comportamento
                                          alternativo. Assim, o programa não será interrompido e a
                                          exceção poderá ser tratada. Chamamos esse processo de captura
                                          da exceção.


    -=- 
        Vamos considerar um exemplo de programa que solicita ao usuário, com a função input(), um número
        inteiro. Embora essa função trate a entrada do usuário como string, é possível utilizá-la em
        conjunto com a função eval() para que os dados inseridos sejam avaliados como
        números. 
    -=-
"""

# num = eval(input('Entre com u número: '))
# print(num)

# Dessa forma, se o usuário entrar com um valor do tipo 'str' irá dar um error irá encerrara execução do programa

"""
    Para solucionar isso, podemos tratar os erros usando Bloco "Try" e o Bloco "exept"
        - Bloco TRY >> É executado primeiramente. Devem ser inseridas nele as instruções do fluxo normal do programa.
        - Bloco EXCEPT >> Só será executado se houver o levantamento de alguma exceção. (Isso permite que o fluxo de execução continue de maneira alternativa. O emulador seguinte mostra uma implementação possível desse exemplo (código 25 no arquivo disponibilizado).)
"""

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
    # Se entrarmos com um nimber, irá execultar esse bloco
except:
    print("Entre com o valor numérico e não letras")
    # Se entrarmos com uma string, irá execultar esse bloco

print('Código finalizado')
# Instrução fora do try/except