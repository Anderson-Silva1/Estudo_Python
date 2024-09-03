"""
    ERROS EM UM PROGRAMA PYTHON >> Vamos agora identificar, compreender e lidar com diferentes tipos de
                                   erros: erros de sintaxe, exceções e falhas de lógica.

    ERROS E EXCEÇÕES >> Até agora consideramos que nossos programas tiveram seu fluxo de execução
                        normal. Entretanto, na prática podem haver exceções, que são erros não
                        previstos, que vão quebrar meu programa.

    TIPOS DE ERROS NO PYTHON:
        - ERRO DE SINTAXE (SyntaxError) >> são aqueles que ocorrem devido ao formato incorreto de uma
                                           instrução. Esses erros são descobertos pelo componente do
                                           interpretador Python, que é chamado analisador ou parser.

        - ERRO DE SINTAXE (IndentationError) >> Quando a indexação está errada
                             
        - ERRO EM TEMPO DE EXECUÇÃO DO PROGRAMA >> que não se devem a uma instrução escrita errada, e
                                                   sim ao fato de que o programa entrou em um estado
                                                   indevido
            * EXEMPLOS:
                - Divisões por 0 (zeros)
                - Tentativa de acessar um índice indevido de uma lista
                - Um nome de variávelnão atribuído
                - Um erro causado por por tipos incorretos de operadores
    
    -=- Em cada caso, quando o programa atinge um estado inválido, é dito que o interpretador Python levanta uma exceção. Isso significa que é criado um objeto que contém as informações relevantes sobre o erro. -=-

    TIPOS COMUNS DE EXEÇÕES:
        1 - KeyboardInterrupt >> Levantado quando o usuário pressiona CTRL+C (a combinação de interrupção).
        2 - OverflowError >> Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
        3 - ZeroDivisionError >> Levantado quando se tenta dividir por 0.
        4 - IOError >> Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
        5 - IndexError >> Levantado quando um índice sequencial está fora do intervalo de índices válidos.
        6 - NameError >> Levantado quando se tenta avaliar um identificador (nome) não atribuído.
        7 - TypeError >> Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
        8 - ValueError >> Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.

    -=- Em Python, as exceções são objetos. A classe Exception é derivada de BaseException, classe base de todas as classes de exceção. BaseException fornece alguns serviços úteis para todas as classes de exceção, mas normalmente não se torna uma subclasse diretamente. -=-
"""