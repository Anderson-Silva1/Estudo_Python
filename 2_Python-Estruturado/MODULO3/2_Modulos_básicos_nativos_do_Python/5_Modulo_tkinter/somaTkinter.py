import tkinter as tk
from tkinter import messagebox

def soma_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    messagebox.showinfo('Resultado', 'A soma dos números é: {}'.format(resultado))

janela = tk.Tk()

janela.title('Calculadora de soma')

label_num1 = tk.Label(janela, text='Numero 1:')
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)


label_num2 = tk.Label(janela, text='Numero 2:')
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao = tk.Button(janela, text='Somar', command=soma_numeros)
botao.grid(row=2, column=2, padx=10, pady=5)

janela.mainloop()

def comp_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num1 > num2 :
       messagebox.showinfo("Resultado", f"O numero {num1} é maior que {num2}")
    elif num1 == num2 :
       messagebox.showinfo("Resultado", f"O numero {num1} é  igual a {num2}")
    else:
       messagebox.showinfo("Resultado", f"O numero {num1} é menor que {num2}")

# Criando a janela
janela2=tk.Tk()
janela2.title("Comparando Numeros")

# Criando os widgets
label_num1=tk.Label(janela2, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1=tk.Entry(janela2)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2=tk.Label(janela2, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2=tk.Entry(janela2)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comp=tk.Button(janela2, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela2.mainloop()
