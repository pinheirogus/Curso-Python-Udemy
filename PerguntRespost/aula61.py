
perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2 + 2?',
        'respostas': {
            'a' : 1,
            'b' : 4,
            'c' : 22,
            'd' : 5,
        },
        'resposta_certa': 'b',
    
    },

    'Pergunta 2' : {
        'pergunta' : 'Quanto é 3 * 2?',
        'respostas': {
            'a' : 1,
            'b' : 4,
            'c' : 6,
            'd' : 5,
        },
        'resposta_certa': 'c',
    
    },

    'Pergunta 3' : {
        'pergunta' : 'Quanto é O + 1?',
        'respostas': {
            'a' : 11,
            'b' : 1,
            'c' : 0,
            'd' : 'O1',
        },
        'resposta_certa': 'd',
    
    },

}

respostas_certas = 0

for chave_primaria, chave_sec in perguntas.items():
    print(f'{chave_primaria}: {chave_sec["pergunta"]}')

    for chave_resp_prim, chave_resp_sec in chave_sec['respostas'].items():
        print(f'\t [{chave_resp_prim}]: {chave_resp_sec} ')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == chave_sec['resposta_certa']:
        print("Parabéins.")
        respostas_certas += 1
    else:
        print('Vish, deu errado.')

    
qtde_perguntas = len(perguntas)

porcentagem_acerto = 100 * (respostas_certas / qtde_perguntas)

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')