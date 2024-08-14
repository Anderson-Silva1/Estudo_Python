# COMPLEX - É o tipo utilizado para manipular números complexos, na forma x + yj, sendo x a parte real e y a parte imaginária do complexo.
c_exNumberComplex1 = complex(5, 2)
print(type(c_exNumberComplex1)) # <class 'complex'>

c_exNumberComplex2 = 5 + 2j
print(type(c_exNumberComplex2)) # <class 'complex'>

#------------------------------------------

# Tranformando outros tipos de dados em "int":
    # Para isso podemos chamar a expressão: int() para fazer a "conversão de tipo" ou "coerção de tipo":

testeString = "123"

print(f"""Estamos pegando uma string:
            {testeString, type(testeString)}

E transformando em Complex:
            {complex(testeString), type(complex(testeString))}""")

#------------------------------------------