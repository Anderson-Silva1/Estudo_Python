"""
    TKINTER >> O pacote tkinter é a interface Python padrão para o Tk GUI (interface gráfica com o usuário) toolkit. Na maioria dos casos, basta importar o próprio tkinter, mas diversos outros módulos estão disponíveis no pacote.

    -- A biblioteca tkinter permite a criação de janelas com elementos gráficos, como a entrada de dados e botões, por exemplo. --
"""

from tkinter import *    # Importamos a biblioteca TKINTER

# Criando uma função
def clicarBotao():
    print('Botão pressionado, 123')

janelaPrincipal = Tk() # CRIAMOS A NOSSA JANELA

# AQUI DENTRO FICARÁ O CONTEÚDO

# Criando um texto
texto = Label(master = janelaPrincipal, text = 'Minha janela exibida')
texto.pack()

# Criando uma imagem
pic = PhotoImage(file='./Anderson.png')
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

# Criando um botão e atribuindo a função a ele quando pressionado
botao = Button(master=janelaPrincipal, text='Clique aqui', command=clicarBotao)
botao.pack()

janelaPrincipal.mainloop() # EXECULTAMOS A NOSSA JANELA