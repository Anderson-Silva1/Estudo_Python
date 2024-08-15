# OPERADORES SEQUÊNCIAIS >> Permitem a manipulação dos tipos sequenciais, inclusive as strings. Vale ressaltar a sobrecarga dos operadores + e *, que realizam operações diferentes quando os operandos são numéricos ou sequenciais.

# EX: O operador "==" verifica se as strings dos dois lados são iguais. Já os operadores "< e >" comparam as strings usando a ordem do dicionário.

"""
    x in s >> TRUE se "x" estiver dentro de "s"
        IN >> Significa "estar dentro"
    x not in s >> FALSE se "x" estiver dentro de "s"
        NOT >> Negação, troca o sentido
    s + t >> Concatena "s" e "t"
        CONCATENAR >> Fazer a junção, no caso de strings, claro... se for um number, será feira a operação matemática
    n*s >> Concatenação de n cópias de s
        N >> Nesse caso é quantas vezes eu quero que o "S" se repita e concatene
            SINTAXE: 5*"Teste " >> teste teste teste teste teste 
    s[i] >> Caractere de índice i em s
        I >> É o index de um elemento, seja uma string, um alista, uma tupla, um dicionario ou qualquer outra estruturade dado do Python
    len(s) >> Comprimento de "S"
        LEN >> Fhnção doPython que vai contar quantos elementos existem dentro de uma determinadaesytrutura de dado
            SINTAXE:
                ELEMENTO:   1          2         3
                lista = ["teste1", "teste2", "teste3",]
                print(len(lista)) >> 3
    min(s) >> Menor item de s
        MIN >> É uma função do Python que vai pegar o menor elemento de uma estrutura de dado
            OBS: 
                - Se for uma string ele vai pela ordem do cabeçalho: A, B, C, D, E...
                - Se for um number ele vai pela ordem de números traduicional...
    max(s) >> Maior item de s
        MAX >> É uma função do Python que vai pegar o maior elemento de uma estrutura de dado
            OBS: 
                - Se for uma string ele vai pela ordem do cabeçalho: A, B, C, D, E...
                - Se for um number ele vai pela ordem de números traduicional...
"""