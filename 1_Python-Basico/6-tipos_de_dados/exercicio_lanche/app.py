hamburguer = 10.50
bauru = 9.50
batafaFrita = 4.00
refrigerante = 3.00

qtd_hamburguer = int(input("Quantos Hamburguer's você quer? "))
qtd_baurus = int(input("Quantos Baurús's você quer? "))
qtd_batatasFrita = int(input("Quantas Batatas Fritas você quer? "))
qtd_refrigerante = int(input("Quantos Refrigerantes você quer? "))

preco_total = (hamburguer * qtd_hamburguer)+(bauru * qtd_baurus)+(batafaFrita * qtd_batatasFrita)+(refrigerante * qtd_refrigerante)

print("Total a pagar é de: R$ {:.2f}".format(preco_total))