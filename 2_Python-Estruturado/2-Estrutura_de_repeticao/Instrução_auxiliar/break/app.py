# BREAK vai parar a verificação seja de uma estrutura de repetição ou uma estrutura de descisão

# É utilizada para interromper as repetições dos laços for e while. Quando o programa encontra uma instrução break, a repetição é encerrada e o fluxo do programa continua a partir da primeira instrução após o laço. Vamos entender como a instrução break funciona!

#--------------------------------------------------------------------------------
# EXEMPLO DE WHILE USANDO BREAK
print("Inicio do while") # Printamos essa informação na tela
while True : # ENQUANTO NOSSA NONDIÇÃO FOR "TRUE" ELE VAI EXECULTAR O QUE ESTÁ DENTRO DO BLOCO DE CÓDIGO
    print("loop") # ENQUANTO NOSSA NONDIÇÃO FOR "TRUE" ELE VAI EXECULTAR ESSE PRINT
    text = input("Deseja sair do programa? então digite sair: ") # ENQUANTO NOSSA NONDIÇÃO FOR "TRUE" ELE VAI EXECULTAR ESSE INPUT
    if text == "sair" : # SE O INPUT FOR "sair" ESSE IF VAI SER EXECULTADO
        print("Saiu do WHILE") # SE O INPUT FOR "sair" ESSE IF VAI SER EXECULTADO: print("Saiu do WHILE")
        break # Esse Break para a nossa verificação, pois queremos sair do programa
#--------------------------------------------------------------------------------
print("")
#--------------------------------------------------------------------------------
# Exemplo com break em laços aninhados

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
               break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

"""
    Vamos analisar, novamente, linha a linha o que esse código realiza. Confira!

    1 - A linha 1 cria o primeiro laço while infinito.
    2 - A linha 2 imprime uma mensagem indicando que o usuário está no primeiro laço.
    3 - A linha 3 solicita ao usuário que insira uma opção.
    4 - A linha 4 verifica se a opção inserida é SIM. Se for, a instrução break é executada, encerrando o primeiro laço while.
    5 - Caso contrário, a linha 6 cria um segundo laço while infinito.
    6 - A linha 7 imprime uma mensagem indicando que o usuário está no segundo laço.
    7 - A linha 8 solicita ao usuário que insira uma opção.
    8 - A linha 9 verifica se a opção inserida é SIM. Se for, a instrução break é executada, encerrando o segundo laço while.
    9 - A linha 11 imprime uma mensagem indicando que o usuário saiu do segundo laço.
    10 - A linha 12 imprime uma mensagem indicando que o usuário saiu do primeiro laço.
"""
#--------------------------------------------------------------------------------

# A instrução break é muito útil quando precisamos sair de um laço antes que ele termine normalmente. Ela pode ser usada tanto em laços while quanto em laços for.