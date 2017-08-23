
# coding: utf-8

# In[57]:

with open('Текстовый файл для ДЗ первое второй модуль.txt', encoding = "utf8") as file:
    content = []
    for line in file:
        cook_book = {}
        name = line.rstrip('\n')
        number_of_ingredients = file.readline().rstrip('\n')
        number_lines_with_ingredients = 0
        
        if '|' in file.readline():
          number_lines_with_ingredients +=1
        
        while number_lines_with_ingredients > 0:
          other_line = file.readline()
          for word in other_line:
            ingredients_book = {}
            divider = other_line.find('|')
            name_ingredient = other_line[:divider]
            next_divider = other_line.find('||')
            volume = other_line[divider+2:next_divider]
            measurer = other_line[next_divider+3:len(other_line)-1]
            number_lines_with_ingredients -=1
            cook_book.update({'Название блюда:', name_ingredient})
            cook_book.update({'Количество ингредиентов:', number_of_ingredients})
            cook_book.update({'Ингредиенты:', ingredients_book})
    print(*content)
