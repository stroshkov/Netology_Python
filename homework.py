import os
import subprocess

def photo_converter(photo_for_resize):
    print('Идет обработка фотографии {}'.format(photo_for_resize))
    subprocess.call('convert {} -resize 200 {}'.format(source_file, result_file))
    print('Обработка фотографии {} завершена'.format(photo_for_resize))

if __name__ == '__main__':
    source = 'Source'
    program = 'convert.exe'
    new_source = 'New_Source'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(current_dir, source)
    list_of_photo = os.listdir(source_path)
    result_path = os.path.join(current_dir, new_source)
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    for photo in list_of_photo:
        source_file = os.path.join(source_path, photo)
        result_file = os.path.join(result_path, photo)
        photo_converter(photo)
