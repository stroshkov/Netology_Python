import os

# В данной директории ошибся при создании папки и не знаю как исправить (папка Migrations в папке Migrations), но код написан как
# будто папка лежит на том же уровне, что и файл homework.py
migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_with_files = os.path.join(current_dir, migrations)
list_of_files = os.listdir(folder_with_files)


def input_text_function():
    input_text = input('Введите часть текста в файле:')
    return input_text


def counting(input_data):
    number_files = 0
    for file in list_of_files:
        text = []
        test_file = os.path.join(folder_with_files, file)

        with open(test_file) as file:
            for line in file:
                text.append(line)

        text_for_search = ' '.join(text)

        if input_data in text_for_search:
            number_files += 1
            print(file)
            index_of_file = list_of_files.index(file)
            list_of_files.pop(index_of_file)

    print(number_files)
    return counting(input_text_function())


counting(input_text_function())
