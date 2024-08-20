# USANDO O SLICING - é uma técnica usada para acessar partes específicas de sequências, como listas, strings ou tuplas

# sintaxe: [ index inicio : index fim : passo (Opicional... O valor padrão é 1) ]

c_exLista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(c_exLista1[ 0 : 9 : 2 ]) # [1, 3, 5, 7, 9]
# Nesse exemplo estamos começando a pegar os ítens da lista no index 0 (1), e vamos até o índex 9 (10), e colocamos um passo de 2 em 2

# OBS: No parâmetro "FIM", não será exibido o elemento do índex de fato, será mostrado sempre até um index a menos...

print("") # Identação

# OUTROS EXEMPLOS

# Index NEG:-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# index:     0  1  2  3  4  5  6  7  8  9
# elemento:  1  2  3  4  5  6  7  8  9  10
c_exLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 - Se queremos pegar a lista toda podemos fazer assim:
print(c_exLista) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# OU
print(c_exLista[ : ]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# OU
print(c_exLista[ : : ]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("") # identação

# 2 - Se queremos pegar de um índice específico até o final podemos fazer assim:
print(c_exLista[4 : ]) # [5, 6, 7, 8, 9, 10]
# OU
print(c_exLista[4 : : ]) # [5, 6, 7, 8, 9, 10]

# Se queremos pegar do primeiro índex até o último index que vamos definir, podemos rfazer assim
print(c_exLista[ : 6]) # [1, 2, 3, 4, 5, 6]
# OU
print(c_exLista[ : 6 :]) # [1, 2, 3, 4, 5, 6]
