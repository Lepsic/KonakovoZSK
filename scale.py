import pandas as pd
from datetime import datetime
from function_transit_data import transition_to_destruction

# Last_name = input('Введите фамилию:_')
# steel_grade = input('Введите марку стали:_')
# temporary_resistance1= input('Введите значение временного сопротивления 1:_')
# temporary_resistance2= input('Введите значение временного сопротивления 2:_')
# temporary_resistance3= input('Введите значение временного сопротивления 3:_')
# постоянные данные
permanent_recording1 = 'Вр. сопр. норма - 380-490'
permanent_recording2 = 'Вр. сопр. норма -  более 490'
permanent_recording3 = 'Годен'
permanent_recording4 = 'Угол загиба 80 градусов'
permanent_recording5 = 'Угол загиба 120 градусов'
permanent_recording6 = 'Не годен'

while True:
    last_name = input("Введите фамилию: ")
    if last_name.isalpha():
        break
    else:
        print("Фамилия должна содержать только буквы. Пожалуйста, введите ее заново.")

while True:
    steel_grade = input("Введите марку стали (СТ3 или 09Г2С): ")
    if steel_grade in ['СТ3', '09Г2С', 'ст3', 'Ст3', '09Г2с', '09г2с', '09г2С', '1']:
        break
    else:
        print("Марка стали должна быть СТ3 или 09Г2С. Пожалуйста, введите его заново.")

while True:
    try:
        temporary_resistance1 = int(input("Введите число для временного сопротивления 1 в кН : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение для временного сопротивления. Пожалуйста, введите его заново.")

while True:
    try:
        temporary_resistance2 = int(input("Введите число для временного сопротивления 2 в кН : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение для временного сопротивления. Пожалуйста, введите его заново.")

while True:
    try:
        temporary_resistance3 = int(input("Введите число для временного сопротивления 3 в кН: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение для временного сопротивления. Пожалуйста, введите его заново.")

while True:
    try:
        sectional_area = int(input("Введите площадь поперечного сечения в мм: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение для площадь поперечного сечения. Пожалуйста, введите его заново.")

temporary_resistance = [temporary_resistance1, temporary_resistance2, temporary_resistance3]
effort_destruction = []

for resistance in temporary_resistance:
    result = transition_to_destruction(resistance)
    effort_destruction.append(result)
effort_destruction1, effort_destruction2, effort_destruction3 = effort_destruction
arithmetic_mean = round((effort_destruction1 + effort_destruction2 + effort_destruction3) / 3, 1)

if steel_grade == 'Ст3':
    if arithmetic_mean >= 380 and arithmetic_mean <= 490:
        test_result = '\n'.join([permanent_recording2, permanent_recording3, permanent_recording4])
    else:
        test_result = permanent_recording6

if steel_grade == '09Г2С':
    if arithmetic_mean >= 490:
        test_result = '\n'.join([permanent_recording1, permanent_recording3, permanent_recording5])
    else:
        test_result = permanent_recording6

current_date = datetime.now()

print('Текущая дата:', current_date)
print('Фамилия_', last_name)
print('Марка стали_', steel_grade)
print("Bременное сопротивление - разрушение 1 = ", temporary_resistance1)
print("Bременное сопротивление - разрушение 2 = ", temporary_resistance2)
print("Bременное сопротивление - разрушение 3 = ", temporary_resistance3)
print("Предел прочости 1 = ", effort_destruction1)
print("Предел прочости 2 = ", effort_destruction2)
print("Предел прочости 3 = ", effort_destruction3)
print("Предел прочости 3 = ", arithmetic_mean)
print("Среднее значение Вр.сопр. = ", arithmetic_mean)
print(test_result)

print('молодец!!!')
