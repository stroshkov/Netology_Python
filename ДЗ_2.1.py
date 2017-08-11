
# coding: utf-8

# In[57]:

with open('Текстовый файл для ДЗ первое второй модуль.txt', encoding = "utf8") as file:
    for line in file:
        content = []
        name = line
        number_of_ingredients = file.readline()
        while '|' in file.readline():
            content.append(file.readline())
        print('Название блюда:', name)
        print('Количество ингредиентов:', number_of_ingredients)
        print('Состав блюда:','\n', *content, end = '')
