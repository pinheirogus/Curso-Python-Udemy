
from string import Template
from datetime import datetime

with open('template.html', 'r', encoding='utf8') as html:
    #Neste caso, o arquivo está sendo lido e passando uma string para a classe Template
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')

    corpo_msg = template.safe_substitute(nome = 'Luiz Otávio', data = data_atual )


print(corpo_msg)