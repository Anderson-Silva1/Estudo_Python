# EVAL

# A função "eval" recebe um dado do tipo "str" e converte ele para o tipo de dado "number" no Python.

c_str = "1 + 4"
print(c_str) # Quando não usamos a função "eval": 1 + 4
print(eval(c_str)) # Quando usamos a funçãop "eval": 5

# Perceba que a função "eval" pegou a "str" "1 + 4" e ao invés de tratar isso como "str" ele tranformou em "number" e fez a operação matemática de: 1 + 4, que dá o resultado: 5.