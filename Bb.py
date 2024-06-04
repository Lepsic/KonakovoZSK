from datetime import datetime
import pandas as pd

f = (input('Введите марку стали: '))
#f = 3,9;
    # if f != (3,9):
    #   print("Переменная x больше 3")
    #else:
    #print("Программа завершена, так как переменная x меньше или равна 10")
    #exit()

n1 = float ( input ('Введите значение временного сопротивления 1:  '))
s1= round ((n1*1000)/160,1)
n2 = float ( input ('Введите значение временного сопротивления 2:  '))
s2= round ((n2*1000)/160,1)
n3 = float ( input ('Введите значение временного сопротивления 3:  '))
s3= round ((n3*1000)/160,1)
q =  round ((s1+s2+s3)/3,1)
if f == '3':
    if q >= 380 and q <= 490:
        d = ('Вр. сопр. норма - 380-490''\n''Годен''\n''Угол загиба 80 градусов')
    else:
        d = ('Не годен')

if f == '9':
    if q >= 490 :
        d = ('Вр. сопр. норма -  более 490''\n''Годен''\n''Угол загиба 120 градусов')
    else:
        d = ('Не годен')

from datetime import datetime
current_date = datetime.now()
print("Текущая дата:", current_date)

print ( "Bременное сопротивление - разрушение = ", s1)
print ( "Bременное сопротивление - разрушение = ", s2)
print ( "Bременное сопротивление - разрушение = ", s3)
print( "Среднее значение Вр.сопр. = ",q)
print(d)

#from datetime import datetime
#import openpyxl
#current_date = datetime.now()
#workbook = openpyxl.load_workbook('example.xlsx')
#sheet = workbook['Лист1']
#sheet['A2'] = current_date
#workbook.save('example.xlsx')
