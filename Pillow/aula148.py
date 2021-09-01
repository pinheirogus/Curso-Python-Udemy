
import os
from PIL import Image

def main(main_images_folder, new_width):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)

            converted_tag = '_Convertido'

            file_name, extension = os.path.splitext(file)
            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe.')
                continue

            if 'Fotos para Su - camera Marina' in file_full_path:
                # img_pillow = Image.open(file_full_path)
                # exif = img_pillow._getexif()
                # print(exif.get(36867))
                # img_pillow.close()
                continue
            if converted_tag in file_full_path:
                os.remove(file_full_path)
                print('Imagem já convertida')
                continue

            #
            # img_pillow = Image.open(file_full_path)
            # exif = img_pillow._getexif()
            #
            # width, height = img_pillow.size
            #
            # new_height = round(new_width * height / width)
            #
            # new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            # new_image.save( new_file_full_path, optimize = True, quality = 70, exif = img_pillow.info['exif'])
            #
            #
            # print(f'{file_full_path} convertido com sucesso!')
            # new_image.close()
            # img_pillow.close()



if __name__ == '__main__':
    main_images_folder = r'D:\Biblioteca\Fotografia'
    main(main_images_folder, new_width=1920)