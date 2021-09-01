from string import Template
from datetime import datetime
from dadosemail import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r', encoding='utf8') as html:
    #Neste caso, o arquivo está sendo lido e passando uma string para a classe Template
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')

    corpo_msg = template.safe_substitute(nome = 'Indalécio', data = data_atual )

msg = MIMEMultipart()
msg['from'] = 'Gustavo Pinheiro'
msg['to'] = 'junioripj@gmail.com'
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as error:
        print('E-mail não enviado...')
        print('Erro: ', error)