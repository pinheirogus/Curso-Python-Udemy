from aula104_classes import Escritor
from aula104_classes import Caneta
from aula104_classes import MaquinaDeEscrever

escritor1 = Escritor('Joãozinho')

canetaBic = Caneta('Bic')

maquina = MaquinaDeEscrever()

# print(escritor1.nome)
# print(canetaBica.marca)
# print(maquina)


escritor1.ferramenta = canetaBic

escritor1.ferramenta.escrever()

escritor1.ferramenta = maquina

escritor1.ferramenta.escrever()