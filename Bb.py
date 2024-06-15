import pandas as pd
from datetime import datetime
source_file = pd.read_excel('Na_treni.xlsx', sheet_name='Лист1')
cell_value_A3 = source_file.iloc[1, 0]
cell_value_A4 = source_file.iloc[2, 0]
cell_value_A5 = source_file.iloc[3, 0]
cell_value_A6 = source_file.iloc[4, 0]
cell_value_A7 = source_file.iloc[5, 0]
cell_value_A8 = source_file.iloc[3, 0]

Last_name = cell_value_A3
steel_grade = cell_value_A4


mark_metal = ['Ст3', '09Г2С']
#if steel_grade in mark_metal:
    #print('its ok')
    #raise ValueError("Такой марки стали не существует")
    # if steel_grade != (Ст3,09Г2С):
    #   print("Переменная x больше 3")
    #else:
    #print("Программа завершена, так как переменная x меньше или равна 10")
    #exit()


temporary_resistance1 = cell_value_A5
effort_destruction1= round ((temporary_resistance1*1000)/160,1)
temporary_resistance2 = cell_value_A6
effort_destruction2= round ((temporary_resistance2*1000)/160,1)
temporary_resistance3 = cell_value_A7
effort_destruction3= round ((temporary_resistance3*1000)/160,1)
arithmetic_mean =  round ((effort_destruction1+effort_destruction2+effort_destruction3)/3,1)
permanent_recording1 = 'Вр. сопр. норма - 380-490'
permanent_recording2 = 'Вр. сопр. норма -  более 490'
permanent_recording3 = 'Годен'
permanent_recording4 = 'Угол загиба 80 градусов'
permanent_recording5 = 'Угол загиба 120 градусов'
permanent_recording6 = 'Не годен'
if steel_grade == 'Ст3':
    if arithmetic_mean >= 380 and arithmetic_mean <= 490:
        test_result = permanent_recording1,'\n', permanent_recording3 ,'\n',permanent_recording4
    else:
        test_result = permanent_recording6

if steel_grade == '09Г2С':
    if arithmetic_mean >= 490 :
        test_result = ('Вр. сопр. норма -  более 490''\n''Годен''\n''Угол загиба 120 градусов')
    else:
        test_result = permanent_recording6


current_date = datetime.now()
print("Текущая дата:", current_date)
print(cell_value_A3,'\n', cell_value_A4,)
print ( "Bременное сопротивление - разрушение = ", effort_destruction1)
print ( "Bременное сопротивление - разрушение = ", effort_destruction2)
print ( "Bременное сопротивление - разрушение = ", effort_destruction3)
print( "Среднее значение Вр.сопр. = ",arithmetic_mean)
print( test_result )

#добавляет данные в файл  results1
final_file = pd.read_excel('results1.xlsx', sheet_name='Лист1')

final_file.at[1, 0] = arithmetic_mean
final_file.at[1, 2] = test_result
source_file.at[1, 2] = arithmetic_mean
source_file.at[1, 3] = current_date


# Создание DataFrame с данными
# данные в постоянно созаваемом новом файле как указывать без тильды?
data = {'Резервный протокол': [current_date, cell_value_A3,cell_value_A4, effort_destruction1,  effort_destruction2, effort_destruction3,  arithmetic_mean , test_result,]}
df = pd.DataFrame(data)

# Запись данных в файл Excel
output_file_name =  datetime.now().strftime('%Y-%m-%d_%H-%M''_') + cell_value_A3+ '.xlsx'
with pd.ExcelWriter(output_file_name) as writer:
    df.to_excel(writer, sheet_name='Sheet1', startrow=1, startcol=0, index=False)

print(f"Данные успешно записаны в файл {output_file_name}")

source_file.to_excel('Na_treni.xlsx', sheet_name='Лист1', index=False)
final_file.to_excel('results1.xlsx', sheet_name='Лист1', index=False)