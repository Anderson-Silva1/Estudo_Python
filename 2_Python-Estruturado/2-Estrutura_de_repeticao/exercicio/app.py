"""
    PROGRAMA EM PYTHON ONDE:
        1 - Pegar todos os números entre 1000 e 9999
        2 - Esses números devem ter a raiz quadrada
            igual a soma dos dois algorismos mais 
            significativos e com os dois algorismos 
            menos significativos.


        NÚMEROS MAIS E MENOS SIGNIFICATIVOS DE 2465:
            MAIS SIGNIFICATIVOS:
                - São os algorismos a esquerda: 24
            MENOS SIGNIFICATIVOS:
                - São os algorismos a direita: 65

        
        SE A SOMA DOS ALGORISMOS MAIS SIGNIFICATIVOS E MENOS SIGNIFICATIVOS FOR A RAÍZ QUADRADA DO TODO, ESSE NÚMERO DEVE SER RETORNADO

        EX:
              24
            + 65
            -----
              89 

        SE 89 FOR A RAÍZ QUADRADA DE 2468, 2465 irá ser retornado ao nosso código

        COMO OBTER ESSES NÚMEROS:
            - Para pegarmos o número menos significativo precisamos pegar o resto da divisão desse número por 100
                SINTAXE: 2465 % 100 >> 65
            - Para pegarmos o número mais significativo precisamos pegara divisão exata desse número por 100
                SINTAXE: 2465 // 100 >> 24
"""

for num in range(1, 10000) :
    mais_s = num // 100
    menos_s = num % 100
    raiz = mais_s + menos_s

    if (raiz * raiz) == num :
        print(f"Esse e o numero: {num}")
        print(f"Esse e o numero menos significativo: {menos_s}")
        print(f"Esse e o numero mais significativo: {mais_s}")
        print(f"Esse e a raiz desse de {num}: {raiz}")
        print("")

print(f"Terminou no {num}")