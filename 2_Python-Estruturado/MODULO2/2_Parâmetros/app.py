"""
    O que são parâmetros em Python??
        >> São os valores que você passa para a função quando a chama
            EX: 
                def soma(num1, num2):
                    print(num1 + num2)
            - Aqui estamos colocando duas variáveis (num1 2 num2) como parâmetros
"""

#----------------------------------------------------------------------------

"""
    Parâmetros em Python >> Quando você cria uma função em Python, ela geralmente precisa de alguns dados para trabalhar. Existem duas maneiras principais para uma função obter esses dados, observe!
        1 - Acessar variáveis globais:
            * Variáveis que estão fora da função, mas que a função consegue ver e usar.
        2 - Passagem de parâmetros:
            * Passar variáveis diretamente para a função quando ela é chamada.

            SINTAXE:
                def teste_funcao ( <parâmetro(s)> ) :
                    <Bloco de código> # NOTE: Aqui eu posso usar os parâmetros para calcular alguma coisa

                teste_funcao(< NOTE: Aqui dentro ficará os parâmetros da nossa função criada acima >)

                
    Usar parâmetros é uma maneira mais segura e flexível de passar dados para a função, pois evita que você altere acidentalmente variáveis globais importantes.


    O que são parâmetros?
        * São os valores que você passa para a função quando a chama
"""
# Vamos ver um exemplo de FUNÇÃO comparâmetro?!
def calculaIMC(peso, altura): # Temos 2 parâmetros: "peso" e "altura"
    return peso / (altura ** 2) # Usamos esses 2 parâmetros para calcular o IMC
print(calculaIMC(60, 1.65)) # Estamos enviando os respectivos parâmetros (peso = 60; altura = 1.65) da Função "calculaIMC"
# Esse acima é o Print completo

print("{:.2f}".format(calculaIMC(60, 1.65))) # Print só com 2 casas decimais

#------------------------------------------------------------------------------------------

"""
    TIPOS DE PARÂMETROS: 
        1 - PARÂMETROS FORMAIS >> São aqueles que você define no cabeçalho da função. 
            No exemplo, peso e altura são parâmetros formais.
            EX: 
                def testeFunc ( <Parâmetetros FORMAIS> ) :
                    return <Retorno>
        
        2 - PARÂMETROS REAIS (ARGUMENTOS) >> São os valores que você passa para a função quando a chama.
            No exemplo, "60, 1.65" são argumentos.
                EX:
                    testeFunc( <Parâmetros Reais ou Argumentos> )


    VALORES DEFAULT PARA PARÂMETROS >> Em Python, você pode definir valores padrão para os parâmetros. Isso é útil quando você quer que um parâmetro tenha um valor padrão se não for fornecido.
        SINTAXE:
            def testeFunct(peso = 60, altura = 1.65) :
                return <Retorno>
            
            * PERCEBA que cada parâmetro Formal dessa função já possui um valor predefinido... Isso significa que caso o usuário não defina valores nos ARGUMENTOS, esse será o valor padrão de uso da função, o que impede que e função gere um erro...
"""
# EXEMPLO DE VALOR PADRÃO PARA PARÂMETROS

def soma(numero1 = 10, numero2 = 20) :
    return numero1 + numero2

print(soma()) # 30, que é a soma de 10 + 20

print(soma(30, 70)) # 100, que é a soma de 30 + 70
# Nesse caso acima os valores padões são substituidos pelos argumentos...