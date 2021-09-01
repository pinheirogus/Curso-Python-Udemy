
from datetime import datetime
from locale import setlocale, LC_ALL

# setlocale(LC_ALL, '')
#  ou
# setlocale(LC_ALL, 'pt_BR.utf-8')
#
# dt = datetime.now()
#
# formatacao1 = dt.strftime('%A, %d de %B de %y')
# formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
#
# print(formatacao1)
# print(formatacao2)
#

#Como retornar o ultimo dia do mês

# from calendar import mdays
#
# dt = datetime.now()
# mes_atual = int(dt.strftime('%m'))
#
# print(mdays)
#
# print(mes_atual, mdays[mes_atual])


# from calendar import monthrange
#
# #Número do dia da semana vai de 0 a 6 - segunda é 0, domingo é 6
# #Abaixo são dados os dias para Fevereiro de 2020.
# dia_semana, ultimo_dia = monthrange(2020, 2)
# print(ultimo_dia)