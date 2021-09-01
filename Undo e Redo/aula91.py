
def adicionar_tarefa(tarefas):
    print('Adicionando tarefas..')
    nova_tarefa = input('Descreva a nova tarefa: ')
    tarefas.append(nova_tarefa)
    return tarefas

def listar_tarefas(tarefas):
    print('Listando tarefas.. ')
    for tarefa in tarefas:
        print(tarefa)
    pass

def desfazer(tarefas):
    print('Desfazendo tarefa')
    try:
        tarefas.pop()
        print('Tarefa removida\n ')
        for tarefa in tarefas:
            print(tarefa)
    except IndexError:
        print("Não há mais tarefas para remover. Tente adicionar uma tarefa.")
    return tarefas

def refazer(tarefas, tarefas_anterior):
    print('Refazendo tarefa')
    try:
        tarefas.append(tarefas_anterior[len(tarefas)])
        for tarefa in tarefas:
            print(tarefa)
    except IndexError:
        print('Tente adicionar uma tarefa.')
    return tarefas

tarefas = []

while True:

    acao = input('O que você gostaria de fazer? Adicionar tarefa, Listar tarefas, Desfazer, Refazer \n')
    if acao[:9] == 'Adicionar' or acao[:9] == 'adicionar':
        tarefas = adicionar_tarefa(tarefas)
        tarefas_anterior = tarefas.copy()
    elif acao[:6] == 'Listar' or acao[:6] == 'listar':
        listar_tarefas(tarefas)
    elif acao[:8] == 'Desfazer' or acao[:8] == 'desfazer':
        tarefas = desfazer(tarefas, tarefas_anterior)
    elif acao[:7] == 'Refazer' or acao[:7] == 'refazer':
        tarefas = refazer(tarefas, tarefas_anterior)
    else:
        print('Favor escolher uma ação válida')

