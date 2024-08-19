# PASS >> Ele vai pular um LOOP

# É usada como um marcador de posição. Ela é útil quando você precisa de uma sintaxe que exige um bloco de código, mas você ainda não decidiu o que escrever nesse bloco. Em outras palavras, pass permite que você escreva uma estrutura que não faz nada, mas mantém a sintaxe correta.

#------------------------------------------------------------------------
for i in range(1, 11) :
    if i % 2 == 0 :
        pass # aqui estamos pulando o numero 5
    else :
        print(i)
print("laco encerrado")

"""
    Vamos verificar o que esse código faz!

        1 - A linha 1 cria um laço for que itera sobre a sequência de números de 1 a 10.
        2 - A linha 2 verifica se o número atual é par (ou seja, divisível por 2 sem resto).
        3 - Se o número for par, a instrução pass é executada, o que significa que nada acontece e o laço continua para a próxima iteração.
        4 - Se o número for ímpar, a linha 6 imprime o número atual.
        5 - Após o laço terminar, a linha 8 imprime a mensagem "Laço encerrado".
"""

# Nesse exemplo, a instrução pass é usada para indicar que nada deve ser feito quando o número é par. Isso ajuda a manter a estrutura do código clara e correta.

# Claramente, seria possível reescrever a condição do if-else para que pudéssemos transformá-lo em um if simples, sem else. Entretanto, o objetivo aqui é mostrar o uso da instrução pass.
#------------------------------------------------------------------------

# Quando o Python encontra a instrução pass, ele simplesmente continua a execução sem fazer nada. Isso pode ser útil em várias situações, como durante o desenvolvimento de código, em que você deseja planejar a estrutura do seu programa antes de preencher os detalhes.