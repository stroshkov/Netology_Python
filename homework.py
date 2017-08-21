# [имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная), сумма оценок за 5 домашних работ (по 10-балльной шкале), оценка за экзамен по 10-балльной шкале]

group = [
  {'first_name': 'Елена', 'second_name': 'Васильева', 'gender': 'мужской', 'coding_skill': 'yes', 'homework': [10, 10, 10, 10, 10], 'exam': [10]},
  {'first_name': 'Антон', 'second_name': 'Соломин', 'gender': 'мужской', 'coding_skill': 'yes', 'homework': [7, 6, 9, 8, 5], 'exam': [7]},
  {'first_name': 'Анастасия', 'second_name': 'Измайлова', 'gender': 'женский', 'coding_skill': 'no', 'homework': [8, 6, 10, 5, 10], 'exam': [5]},
  {'first_name': 'Олег', 'second_name': 'Петров', 'gender': 'мужской', 'coding_skill': 'yes', 'homework': [7, 8, 9, 10, 8], 'exam': [9]},
  {'first_name': 'Арсений', 'second_name': 'Кривов', 'gender': 'мужской', 'coding_skill': 'no', 'homework': [5, 4, 9, 4, 5], 'exam': [5]},
  {'first_name': 'Елена', 'second_name': 'Васильева', 'gender': 'женский', 'coding_skill': 'no', 'homework': [10, 10, 10, 10, 10], 'exam': [10]},
  {'first_name': 'Екатерина', 'second_name': 'Бобова', 'gender': 'женский', 'coding_skill': 'yes', 'homework': [7, 5, 9, 10, 5], 'exam': [10]},
  {'first_name': 'Мария', 'second_name': 'Иванова', 'gender': 'женский', 'coding_skill': 'no', 'homework': [5, 7, 5, 4, 5], 'exam': [5]},
  {'first_name': 'Регина', 'second_name': 'Крылова', 'gender': 'женский', 'coding_skill': 'no', 'homework': [6, 6, 6, 4, 5], 'exam': [6]},
  {'first_name': 'Евгений', 'second_name': 'Семенов', 'gender': 'мужской', 'coding_skill': 'no', 'homework': [7, 6, 9, 4, 5], 'exam': [6]},
  ]

print('Существуют следующие команды:','\n'
'Средняя оценка за домашние задания по группе: X','\n'
'Средняя оценка за экзамен: Y','\n'
'Средняя оценка за домашние задания у мужчин: A','\n'
'Средняя оценка за экзамен у мужчин: B','\n'
'Средняя оценка за домашние задания у женщин: C','\n'
'Средняя оценка за экзамен у женщин: D','\n'
'Средняя оценка за домашние задания у студентов с опытом: E','\n'
'Средняя оценка за экзамен у студентов с опытом: F','\n'
'Средняя оценка за домашние задания у студентов без опыта: G','\n'
'Средняя оценка за экзамен у студентов без опыта: H','\n'
'Фамилия лучшего студента: L','\n')
 
type_of_comand = input("Введите пожалуйста команду")

def calculator_wuth_attribute(female_or_male_or_all, type_work, coders_or_noob_or_all):
  score = 0
  number = 0
  for student in group:
    if type_work == 'homework':
      if coders_or_noob_or_all == 'all':
        if female_or_male_or_all != 'all' and student['gender'] == female_or_male_or_all:
          score += sum(student[type_work])
          number += len(student[type_work])
        if female_or_male_or_all == 'all':
          score += sum(student[type_work])
          number += len(student[type_work])        
      if coders_or_noob_or_all == 'coders':
        if student['coding_skill'] == 'yes':
          score += sum(student[type_work])
          number += len(student[type_work])
      if coders_or_noob_or_all == 'noob':
        if student['coding_skill'] == 'no':
          score += sum(student[type_work])
          number += len(student[type_work])
    if type_work == 'exam':
      if coders_or_noob_or_all == 'all':
        if female_or_male_or_all != 'all' and student['gender'] == female_or_male_or_all:
          score += sum(student[type_work])
          number += 1
        if female_or_male_or_all == 'all':
          score += sum(student[type_work])
          number += 1               
      if coders_or_noob_or_all == 'coders':
        if student['coding_skill'] == 'yes':
          score += sum(student[type_work])
          number += 1
      if coders_or_noob_or_all == 'noob':
        if student['coding_skill'] == 'no':
          score += sum(student[type_work])
          number += 1          
  return score, number

def all_homework():
  result = calculator_wuth_attribute('all', 'homework', 'all')[0] / calculator_wuth_attribute('all', 'homework', 'all')[1]
  return result

def all_exam():
  result = calculator_wuth_attribute('all', 'exam', 'all')[0] / calculator_wuth_attribute('all', 'exam', 'all')[1]
  return result
  
def homework_male():
  result = calculator_wuth_attribute('мужской', 'homework', 'all')[0] / calculator_wuth_attribute('мужской', 'homework', 'all')[1]
  return result

def exam_male():
  result = calculator_wuth_attribute('мужской', 'exam', 'all')[0] / calculator_wuth_attribute('мужской', 'exam', 'all')[1]
  return result    

def homework_female():
  result = calculator_wuth_attribute('женский', 'homework', 'all')[0] / calculator_wuth_attribute('женский', 'homework', 'all')[1]
  return result   

def exam_female():
  result = calculator_wuth_attribute('женский', 'exam', 'all')[0] / calculator_wuth_attribute('женский', 'exam', 'all')[1]
  return result   

def homework_coders():
  result = calculator_wuth_attribute('all', 'homework', 'coders')[0] / calculator_wuth_attribute('all', 'homework', 'coders')[1]
  return result   

def exam_coders():
  result = calculator_wuth_attribute('all', 'exam', 'coders')[0] / calculator_wuth_attribute('all', 'exam', 'coders')[1]
  return result   

def homework_non_coders():
  result = calculator_wuth_attribute('all', 'homework', 'noob')[0] / calculator_wuth_attribute('all', 'homework', 'noob')[1]
  return result   

def exam_non_coders():
  result = calculator_wuth_attribute('all', 'exam', 'noob')[0] / calculator_wuth_attribute('all', 'exam', 'noob')[1]
  return result   

def best_student():
  number_for_text = 0
  number = 0
  dict_for_best_student = {}
  for student in group:
    average_homework = sum(student['homework'])
    exam = sum(student['exam'])
    whole_mark = (0.6 * average_homework) + (0.4 * exam)
    number_for_text +=1
    full_name = 'Студент №', number_for_text, student['first_name'] + '_' + student['second_name']
    dict_for_best_student.update({full_name: whole_mark})
  values = dict_for_best_student.values()
  dict_for_return = []
  for full_name, whole_mark in dict_for_best_student.items():
    if whole_mark == max(values):
      number +=1
      dict_for_return.append(full_name)
  for full_name, whole_mark in dict_for_best_student.items():
    if whole_mark == max(values) and number == 1:
      return ('Лучшим студентом является:', full_name)
    if whole_mark == max(values) and number > 1:
      print('Лучшими студентами являются:')
      for i, best_students in enumerate(dict_for_return):
        print(*best_students)
      return 'Количество студентов с наивысшими оценками:', number

if 'X' == type_of_comand:
  print(all_homework())
elif 'Y' == type_of_comand:
  print(all_exam())
elif 'A' == type_of_comand:
  print(homework_male())  
elif 'B' == type_of_comand:
  print(exam_male())
elif 'C' == type_of_comand:
  print(homework_female()) 
elif 'D' == type_of_comand:
  print(exam_female())  
elif 'E' == type_of_comand:
  print(homework_coders())  
elif 'F' == type_of_comand:
  print(exam_coders())  
elif 'G' == type_of_comand:
  print(homework_non_coders())  
elif 'H' == type_of_comand:
  print(exam_non_coders())  
elif 'L' == type_of_comand:
  print(*best_student())  
else:
  print ("Команда введена некорректно")
