
import os
import shutil

caminho_original = r'C:\Users\Gustavo\Desktop\Legendas temp'
caminho_novo = r'C:\Users\Gustavo\Desktop\Legendas temp criada Python'

try:
    os.mkdir(caminho_novo)
except FileExistsError as error:
    print(f'A pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)

        new_file_path = os.path.join(caminho_novo, file)

        # shutil.move(old_file_path, new_file_path)
        # shutil.copy(old_file_path, new_file_path)

        # print(f'Arquivo {file} copiado com sucesso.')

        if '.zip' in file:
            os.remove(new_file_path)
            print(f'Arquiivo {file} removido com sucesso.')