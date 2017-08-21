documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}, {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]
directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}

def who_by_number():
  number = input("Скажите пожалуйста номер документа")
  for document in documents:
    for key, value in document.items():
      if key == 'number' and value == number:
        return ('Владелец этого документа', document['name'])

def all_date_about_document():
  for document in documents:
    return (document['type'], document['number'], document['name'])

def search_number_of_directories():
  number = input("Скажите пожалуйста номер документа")
  for key, value in directories.items():
    if number in value:
        return 'Документ на {}-ой полке'.format(key)

def add_new_document():
  type = input("Скажите пожалуйста тип документа")
  number = input("Скажите пожалуйста номер документа")
  name = input("Скажите пожалуйста ваше имя")
  directory = input("Скажите пожалуйста на какую из трех полок (1, 2 или 3) его положить")
  
  new_document = {}
  new_document['type'] = type
  new_document['number'] = number
  new_document['name'] = name
  documents.append(new_document)
  
  for key, value in directories.items():
    if directory in key:
      directories[key].append(number)
    else:
      continue
      
  print('Дальше будет проверка добавился ли документ')
  print('Ниже отображается список документов:')
  print(*documents)
  print('Ниже отображается то, какие номера документов на каких полках лежат')
  return directories

def delete_document():
  number = input("Скажите пожалуйста номер документа")
  for document in documents:
    for key, value in document.items():
      if key == 'number' and value == number:
        documents.pop(documents.index(document))
  return ('Проверка для документов:', '\n',documents,'Проверка для полок:', '\n',directories)
  
def add_shelf():
  number = input("Скажите пожалуйста номер новой полки")
  directories.setdefault(number, [])
  return (directories)

type_of_comand = input("Введите пожалуйста команду")

if 'p' == type_of_comand:
  print(who_by_number())
elif 'l' == type_of_comand:
  print(all_date_about_document())
elif 's' == type_of_comand:
  print(search_number_of_directories())  
elif 'a' == type_of_comand:
  print(add_new_document())
elif 'd' == type_of_comand:
  print(delete_document()) 
elif 'as' == type_of_comand:
  print(add_shelf())  
else:
  print ("Команда введена некорректно")
