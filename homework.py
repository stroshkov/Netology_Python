# Необходимо реализовать классы животных на ферме:
#
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

class Animals:
    presence_of_wings = None
    presence_of_horns = None
    legs = 4


    def __init__(self, name):
        self.name = name


    def ability_to_defend(self):
        return 'Животное способно защищаться' if self.presence_of_horns == True else 'Животное беззащитно'


    def giving_eggs(self):
        return 'Животное способно нести яица' if self.presence_of_wings and not self.presence_of_horns \
                                                 and self.legs == 2 else 'Животное не способно нести яица'


    def voice(self):
        return self.text_of_voice


    def print_name(self):
        return 'Животное зовут', self.name


class Cows(Animals):
    presence_of_horns = True
    text_of_voice = "Muuu"


class Goats(Animals):
    presence_of_horns = True
    text_of_voice = "Beee"


class Sheeps(Animals):
    presence_of_horns = True
    text_of_voice = "Baaaaa"


class Pigs(Animals):
    text_of_voice = "Hruuuu"


class Ducks(Animals):
    presence_of_wings = True
    text_of_voice = "Qua Qua"
    legs = 2


class Chickens(Animals):
    presence_of_wings = True
    text_of_voice = "Kud ku dah"
    legs = 2


class Gooses(Animals):
    presence_of_wings = True
    text_of_voice = "Ga ga ga"
    legs = 2

animal_1 = Gooses('Ivan')
print(*animal_1.print_name())
print('У животного есть рога - ', animal_1.presence_of_horns)
print('Животное издает следующие звуки - ', animal_1.voice(), '\n')


animal_2 = Goats('Ivan')
print(*animal_2.print_name())
print('У животного есть рога - ', animal_2.presence_of_horns)
print('Животное издает следующие звуки - ', animal_2.voice(), '\n')

animal_3 = Cows('Ivan')
print(*animal_3.print_name())
print('У животного есть рога - ', animal_3.presence_of_horns)
print('Животное издает следующие звуки - ', animal_3.voice(), '\n')
