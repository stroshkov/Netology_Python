import os

# В данной директории ошибся при создании папки и не знаю как исправить (папка Migrations в папке Migrations), но код написан как
# будто папка лежит на том же уровне, что и файл homework.py
if  __name__ ==  "__main__" :
    # читаем файлы из папки и добавляем их в list_of_files
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_with_files = os.path.join(current_dir, migrations)
    list_of_files = []
    list_of_all_files = os.listdir(folder_with_files)

    for file in list_of_all_files:
        if file.endswith('sql'):
            list_of_files.append(file)

    # прописываем функцию, которая создает переменную input_text из напечатанного текста
    def input_text_function():
        input_text = input('Введите часть текста в файле:')
        return input_text


    def counting(input_data):
        # создаем базовый список, куда будем добаавлять файлы с совпадением, чтобы считать их кол-во
        base_text = []
        # цикл для чтения каждого файла
        for file in list_of_files:
            # строим путь к файлу
            test_file = os.path.join(folder_with_files, file)
            text = []
            # читаем содержимое файла
            with open(test_file) as file:
                text.append(file.read())

            # делаем из списка единую строку с разделителем пробел
            text_for_search = ' '.join(text)

            # проверяем есть ли набранный текст внутри определенного файла и если да, то выводим его название
            if input_data in text_for_search:
                base_text.append(file)
                print(file)
                index_of_file = list_of_files.index(file)
                list_of_files.pop(index_of_file)

        print(len(base_text))
        return counting(input_text_function())


    counting(input_text_function())
