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
        if self.presence_of_horns == True:
            return 'Животное способно защищаться'
        if self.presence_of_horns == False:
            return'Животное беззащитно'


    def giving_eggs(self):
        if self.presence_of_wings == True and self.presence_of_horns == False \
                and self.legs == 2:
            return 'Животное способно нести яица'
        else:
            return 'Животное не способно нести яица'


    def voice(self, text_of_voice):
        print(text_of_voice)


    def print_name(self, name):
        return 'Животное зовут', name


class Cows(Animals):
    presence_of_wings = False
    presence_of_horns = True
    text_of_voice = "Muuu"


class Goats(Animals):
    presence_of_wings = False
    presence_of_horns = True
    text_of_voice = "Beee"


class Sheeps(Animals):
    presence_of_wings = False
    presence_of_horns = True
    text_of_voice = "Baaaaa"


class Pigs(Animals):
    presence_of_wings = False
    presence_of_horns = False
    text_of_voice = "Hruuuu"


class Ducks(Animals):
    presence_of_wings = True
    presence_of_horns = False
    text_of_voice = "Qua Qua"
    legs = 2


class Chickens(Animals):
    presence_of_wings = True
    presence_of_horns = False
    text_of_voice = "Kud ku dah"
    legs = 2


class Gooses(Animals):
    presence_of_wings = True
    presence_of_horns = False
    text_of_voice = "Ga ga ga"
    legs = 2
