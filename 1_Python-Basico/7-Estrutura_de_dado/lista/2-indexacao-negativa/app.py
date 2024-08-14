# Indexação NEGATIVA - Podemos pegar indices negativos em PYTHON, o que básicamente vai fazer é mudar a ordem da lista, ou seja, vai inverter a lista...
# OBS: -1 == A quantidade de Elementos dessa lista, se a lista tiver 5 elementos, -1 vai ser referente ao elemento 5

# ELEMENTO         1            2           3
# INDEX           -3           -2          -1
c_exLista1 = ["Anderson", "Rafaela", "Emanoel"]
print(c_exLista1[-1]) # Emanoel

# ELEMENTO    1  2  3  4  5 
# INDEX      -5 -4 -3 -2 -1 
c_exLista2 = [1, 2, 3, 4, 5]
print(c_exLista2[-4]) # 2

# ELEMENTO     1    2   3
# INDEX       -3   -2  -1
c_exLista3 = [1.0, 2.5, 3.7]
print(c_exLista3[-2]) # 2.5

# ELEMENTO     1     2
# INDEX       -2    -1
c_exLista4 = [True, False]
print(c_exLista4[-1]) # False

# ELEMENTO      1        2     3    4     5
#              -5       -4     -3  -2    -1
c_exLista5 = [True, "Anderson", 1, 3.4, False]
print(c_exLista5[-2]) # 3.4