"""
    O que são Métodos de passagens de parâmetros??
        - São as maneiras existentes para transmiti-los ou recebê-los dos subprogramas chamados.

    Os parâmetros podem ser passados principalmente pelos seguintes métodos:
        1 - Valor >> O parâmetro formal funciona como uma variável local do subprograma, sendo inicializado com o valor do parâmetro real. Dessa maneira, não ocorre uma alteração na variável externa ao subprograma caso ela seja passada como parâmetro.
        2 - Referência >> Em vez de passar o valor do parâmetro real, é transmitido um caminho de acesso (normalmente, um endereço) para o subprograma chamado. Isso fornece o caminho de acesso para a célula que armazena o parâmetro real. Assim, o subprograma chamado pode acessar esse parâmetro na unidade de programa chamadora.

    NOTE: O método de passagem de parâmetros de Python é chamado de passagem por atribuição. Como todos os valores de dados são objetos, toda variável é uma referência para um objeto.
"""

