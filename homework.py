day_cost = 100 #EUR

euro = 67.5
day_cost_rub = 100 * euro #RUB

trips_count = 3
trip_lenght_1 = 10
trip_lenght_2 = 15
trip_lenght_3 = 7

flight_cost = 50
flights_per_trip = 2

trip_cost =(trip_lenght_1 + trip_lenght_2 + trip_lenght_3) * day_cost
trip_cost += flight_cost * flights_per_trip * trips_count

trip_cost_rub = trip_cost * euro

print ('Текущий курс евро -', euro, 'рублей за 1 евро')
print ('В отпуске мы потратим только на перелет', trip_cost, 'EUR или', trip_cost_rub, 'RUB')

ivan_salary = [10000, 10000, 10000]
anna_salary = [400, 0, 1500]
sum_ivan_salary = sum(ivan_salary)
sum_anna_salary = sum(anna_salary)
sum_sum_salary = sum_ivan_salary + sum_anna_salary
sum_sum_salary_rub = sum_sum_salary * euro

print ('Зарплата Ивана и Анны', sum_sum_salary, 'EUR или', sum_sum_salary_rub, 'RUB')

budget_trip_rub = 1000000
ivan_cost = [1000, 5000, 3000] #RUB
anna_cost = [5000, 0, 5000] #RUB
sum_anna_cost = sum(anna_cost)
sum_ivan_cost = sum(ivan_cost)
budget_after_cost_and_trip_rub = budget_trip_rub - trip_cost_rub - sum_ivan_cost - sum_anna_cost

print ('Иван потратил дополнительно', sum_ivan_cost, 'RUB')
print ('Анна потратила дополнительно', sum_anna_cost, 'RUB')
print ('У нас осталось', budget_after_cost_and_trip_rub, 'RUB')

#Дополнительное задание - как калькулятор 

if budget_after_cost_and_trip_rub >= 0:
  print ('Мы не только сможем полететь в отпуск, но и потратить столько, сколько захотим')
elif budget_after_cost_and_trip_rub < trip_cost_rub:
  print ('Мы конечно летим в отпуск, но не сможем потратить столько, сколько хотели')
elif budget_trip_rub >= trip_cost_rub:
  print ('Ну хотя бы мы можем полететь в отпуск')
else:
  print ('Все очень плохо - нам не хватает даже на перелет')
