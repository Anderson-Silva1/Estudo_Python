"""
    SMTPLIB >> Define um objeto de sessão do cliente SMTP que pode ser usado a fim de enviar e-mail para qualquer máquina da internet com um serviço de processamento SMTP ou ESMTP.

    Como a Google não permite, por padrão, realizar o login com a utilização do smtplib por considerar esse tipo de conexão mais arriscada, será necessário alterar uma configuração de segurança. Para resolver isso, siga as instruções a seguir.
        1 - Acesse sua conta no Google.
        2 - Depois acesse Segurança.
        3 - Você precisa habilitar a Verificação em duas etapas
        4 - Criar uma senha de Aplicativo (Para usar no código)
"""


#import dos pacotes necessários
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python, para teste"

#parâmetros
senha = "obhkunnrfieerjjn"
msg['From'] = "anderson.developer360@gmail.com"
msg['To'] = "anderson.developer360@gmail.com"
msg['Subject'] = "Teste envio e-mail Python"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# As linhas 32 e 33 mostram a criação do servidor e a sua conexão no modo TLS.

#Login na conta para envio
server.login(msg['From'], senha)
# A linha 37 mostra o login na conta de origem do e-mail.

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())
# A linha 41 representa o envio propriamente dito.

#encerramento do servidor
server.quit()
# A linha 45 exibe o encerramento do servidor.

print('Mensagem enviada com sucesso')

# PESQUISAR MAIS A FUNDO DEPOIS...