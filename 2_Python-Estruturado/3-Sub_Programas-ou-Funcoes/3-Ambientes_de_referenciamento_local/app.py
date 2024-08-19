"""
    Ambientes de referenciamento local:
        Variáveis locais >> Quando um subprograma define as próprias variáveis, ele estabelece ambientes de referenciamento local. Essas variáveis são chamadas de variáveis locais, nas quais seu escopo usualmente é o corpo do subprograma... São variáveis que serão usadas apenas dentro do subprograma

            1 - DInâmicas a Pilha >> São vinculadas ao armazenamento no início da execução do subprograma
            e desvinculadas quando essa execução termina. As variáveis locais dinâmicas da pilha têm diversas
            vantagens, e a principal delas é a flexibilidade. Suas principais desvantagens são o custo do tempo
            – para alocar, inicializar (quando necessário) e liberar tais variáveis para cada chamada ao 
            subprograma – e o fato de que os acessos a essas variáveis locais devem ser indiretos, enquanto os
            acessos às variáveis estáticas podem ser diretos.

            2 - Estáticas >> São vinculadas a células de memória antes do início da execução de um programa
            e permanecem vinculadas a essas mesmas células até que a execução do programa termine. Elas são
            um pouco mais eficientes que as variáveis locais dinâmicas da pilha, já que não é necessário tempo
            para alocar ou liberar essas variáveis. Sua maior desvantagem é a incapacidade de suportar recursão.

            # NOTA: Todas as variáveis locais em Python são dinâmicas da pilha

            # NOTA: As variáveis globais são declaradas em definições de método; além disso, qualquer variável
              declarada global em um método precisa ser definida fora dele. Caso haja uma atribuição à variável
              local com o mesmo nome de uma variável global, a global é implicitamente declarada como local



              Subprogramas aninhados


              CONTINUAR DEPOIS 

              ORGANIZAR ESSE ARQUIVO DEPOIS.....
"""