# CONTINUE >> É uma instrução auxiliar que vai pular o loop daquele momento

# É usada para pular a iteração atual de um laço e passar para a próxima iteração. Diferente da instrução break, que encerra completamente o laço, a instrução continue apenas interrompe a iteração corrente e continua o laço desde o início.

#------------------------------------------------------------------------
for i in range(1, 11) :
    if i == 5 :
        continue # aqui estamos pulando o numero 5
    else :
        print(i)
print("laco encerrado")

"""
    Analisando linha a linha do código, observamos que:

        1 - A linha 1 cria um laço for que itera sobre a sequência de números de 1 a 10.
        2 - A linha 2 verifica se o número atual é 5.
        3 - Se o número atual for 5, a instrução continue é executada, pulando o restante do bloco do laço e iniciando a próxima iteração.
        4 - Caso contrário, a linha 5 imprime o número atual.
        5 - Após o laço terminar, a linha 7 imprime a mensagem "Laço encerrado".
"""
#------------------------------------------------------------------------

# Quando o Python encontra a instrução continue, ele ignora todas as instruções restantes no laço para aquela iteração e vai direto para a próxima iteração. Isso é útil quando você deseja pular certos valores ou condições dentro de um laço.

# Com os exemplos, podemos ver claramente como continue permite pular uma iteração específica sem interromper todo o laço, enquanto break encerra o laço por completo.