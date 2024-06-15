import pandas as pd
from datetime import datetime

# Чтение файла results1.xlsx и запись данных в лист1, ячейку А2
data = {'Header': ['result']}
df = pd.DataFrame(data)
writer = pd.ExcelWriter('output_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Сохранение в новый excel файл с добавлением даты и времени
writer.save()