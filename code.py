import json

name = input('Введите имя json файла (без "json")')

with open(name + '.json', 'r', encoding = "utf8") as file:
  data = json.load(file)

content = []

#проходим в "нижние уровни" файла, чтобы дойти до самого текста
for first_key, first_value in data.items():
  second_stage = first_value

for second_key, second_value in second_stage.items():
  if 'channel' in second_key:
    third_stage = second_value

for third_key, third_value in third_stage.items():
  if 'items' in third_key:
    fourth_stage = third_value

#создаем список, где каждый элемент - это текст (один элемент = один источник текста)
for news in fourth_stage:
  for news_key, news_value in news.items():
    if 'description' in news_key:
      news_for_analysis = news_value
      content.append(news_for_analysis)

#объединяем список в строку, разделяя элементы пробелом, и потом создаем список из слов
dirty_data_for_analysis = ' '.join(content)
clean_data_for_analysis = dirty_data_for_analysis.split(' ')

#создаем словарь из слов с более чем 6 буквами, где ключ - это слово, а значение  - это сколько раз оно встречается в тексте
total_dictionary = {}

for words in clean_data_for_analysis:
  if len(words) > 6:
    number = clean_data_for_analysis.count(words)
    total_dictionary.update({words: number})

#сортируем словарь по убыванию значения    
result = sorted(total_dictionary.items(), key=lambda item: item[1], reverse=True)

number_for_top_result = 10

print("ТОП 10 по упоминаемости слов в тексте:")

#выводим ТОП 10 слов по популярности
for elements_for_print in result:
  if number_for_top_result > 0:  
    print(elements_for_print[0], '-', elements_for_print[1], 'слов')
    number_for_top_result -=1
  if number_for_top_result <= 0:
    break
