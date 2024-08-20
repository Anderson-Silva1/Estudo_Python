"""
    Objetos range >> é um tipo de objeto que gera uma sequência de números inteiros.
                     Ele é comumente usado em loops for para iterar sobre uma série de números.
                     O objeto range é eficiente em termos de memória, pois não gera todos os
                     números de uma vez; ao invés disso, ele gera os números conforme necessário.
    
    CRIAÇÃO DO RANGE >> Podemos ter 3 parâmetros:
                            1 - STOP (Parar)
                            2 - START (Início)
                            3 - STEP (Passo)
"""

"""
    CASO NOSSO OBJETO RANGE POSSUA APENAS UM PARÂMETRO:
        - Esse único parâmetro será o "STOP":
            
            for i in range(5):
                print(i)

        - Nesse nosso exemplo, nossa lista Range irá finalizar ou parar (STOP) no elemento 5, no index 4 (Na programação em Python, os index iniciam no 0 (zero)) e iniciará por padrão que é 0
"""
for i in range(5):
    print(i)

print("")
"""
    CASO NOSSO OBJETO RANGE POSSUA DOIS PARÂMETROS:
        - O primeiro parâmetro será o "START" e o segundo parâmetro será o "STOP":
            
            for i in range(2, 10):
                print(i)

        - Nesse nosso exemplo, nossa lista Range irá iniciar no número 2 (Sendo ele o index 0) e irá contar até o número 10 (sendo ele o index 7)
"""

for i in range(2, 10):
    print(i)

print("")

"""
    CASO NOSSO OBJETO RANGE POSSUA TRÊZ PARÂMETROS:
        - O primeiro parâmetro será o "START", o segundo parâmetro será o "STOP" e o terceiro será o "STEP":
            
            for i in range(6, 22, 2):
                print(i)

        - Nesse nosso exemplo, nossa lista Range irá iniciar no número 6 (Sendo ele o index 0), irá contar até o número 20 (sendo ele o index 7) e irá cointar de 2 em 2 segundo o terceiro parâmetro... Porém não irá contar o último elemento!!!
"""

for i in range(6, 22, 2):
    print(i)