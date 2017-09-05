
# coding: utf-8

# In[57]:

def get_cookbook():
  with open('cookbook.txt', 'r') as file:
    cookbook = {}  
    
    for line in file:
      dirty_dish_name = line.lower()
      dish_name = dirty_dish_name.strip()
      cookbook[dish_name] = []
      count_of_ingridients = int(file.readline())
      
      for i in range(count_of_ingridients):
        ingridient = {}
        temp_ingridient = file.readline().split(' | ')
        ingridient['Название_ингредиента'] = temp_ingridient[0].strip()
        ingridient['Количество'] = int(temp_ingridient[1].strip())
        ingridient['Единица измерения'] = temp_ingridient[2].strip()
        cookbook[dish_name].append(ingridient)
        
    return cookbook
 
 
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cookbook = get_cookbook()
    for dish in dishes:
        for ingridient in cookbook[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['Количество'] *= person_count
            if new_shop_list_item['Название_ингредиента'] not in shop_list:
                shop_list[new_shop_list_item['Название_ингредиента']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['Название_ингредиента']]['Количество'] += new_shop_list_item['Количество']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['Название_ингредиента'], shop_list_item['Количество'],
                                shop_list_item['Единица измерения']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
