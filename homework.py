import os
import subprocess

source = 'Source'
program = 'convert.exe'
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_with_photo = os.path.join(current_dir, source)
list_of_photo = os.listdir(folder_with_photo)
program_path = os.path.join(current_dir, program)

# создадим папку куда будут отправляться новые файлы
os.mkdir(os.path.join((current_dir, new_source)))

# пройдем по всем фотографиям и дадим названи новым фотографиям в формате от 1 до 5
for photo in list_of_photo:
    args = [program_path, file, '-resize', '200', file]
    proc = Popen(args)
