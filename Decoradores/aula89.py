#
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Estou decorada.')
#         funcao(*args, **kwargs)
#
#     return slave
#
# # Decorador é o comando abaixo
# @master
# def fala_oi():
#     print('Oi')
#
#
# #variavel = master(fala_oi)
#
# fala_oi()

#######################################################################################################################
#
# from time import time
# from time import sleep
#
#
# def velocidade(funcao):
#     def interna(*args, **kwargs):
#         start_time = time()
#         resultado = funcao(*args, **kwargs)
#         end_time = time()
#         tempo = (end_time - start_time) * 1000
#         print(f'\nA função {funcao.__name__} '
#               f'levou {tempo:.2f} ms para executar')
#         return resultado
#
#     return interna
#
#
# @velocidade
# def demora():
#     for i in range(5):
#         print(i)
#         sleep(0.5)
#
# demora()