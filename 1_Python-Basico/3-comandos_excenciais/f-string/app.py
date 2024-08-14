""" f-string - Esse é um novo recurso que veio incluso na versão 3.6 do Python
    nele conseguimos juntar String's com dados em Python"""
''' SINTAXE: f"" > Dentro das áspas eu coloco o meu texto e quando eu
    quiser pegar um dado do Python ou abro chaves "{}"   '''

c_nome: str = "Anderson"
c_idade: int = 19
c_altura: float = 1.65

c_saida_formatada = f"Nome: {c_nome}, idade: {c_idade}, altura: {c_altura}"

print(c_saida_formatada)