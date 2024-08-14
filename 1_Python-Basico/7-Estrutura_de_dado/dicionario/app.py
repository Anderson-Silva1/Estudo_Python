# DICIONÁRIOS - Uma coleção não ordenada, multável e que não permite valores duplicados

#  DICIONÁRIOS - Os dicionários permitem que itens de uma sequência recebam índices definidos pelo usuário. Um dicionário contém pares de (chave, valor). O formato geral de um objeto dicionário é:
c_exDicionario1 = {
                    "name": {
                        "principal": "Anderson",
                        "SobreNome": "Silva"},
                    "nasc": 2004,
                    "gereno": "Masculino"
}
print(c_exDicionario1)
print(c_exDicionario1["nasc"])

#------------------------------------------------------------------

# Selecionando uma chave no Dicionário:
print(f'Selecionando a chave "Genero" do nosso dicionario: {c_exDicionario1["gereno"]}')

#------------------------------------------------------------------

#------------------------------------------------------------------

# Selecionando o valor de uma chave dentro de outra chave:
print("Chamando o valor de uma chave dentro de outra chave: " + c_exDicionario1["name"]["principal"])
print("Chamando o valor de uma chave dentro de outra chave: " + c_exDicionario1["name"]["SobreNome"])

#------------------------------------------------------------------

#------------------------------------------------------------------

# Podemos modificar os valores das chaves no Python:

c_exDicionario1["teste"] =  "teste123" # A chave "teste" não existe no nosso dicionário, mas escrevendo dessa forma nós podemos criá-la
print("Chamando o valor da nossa chave 'teste' que acabou de ser criada: " + c_exDicionario1["teste"]) # Estamos Chamando essa chave que foi modificada

#------------------------------------------------------------------