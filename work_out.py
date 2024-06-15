import pandas as pd
from datetime import datetime

source_file = pd.read_excel('Na_treni.xlsx', sheet_name='Лист1')

cell_value_A2 = source_file.iloc[1, 0]
cell_value_A4 = source_file.iloc[3, 0]
result = cell_value_A4 * 4

print(cell_value_A2, cell_value_A4, result)

final_file = pd.read_excel('results1.xlsx', sheet_name='Лист1')

final_file.at[1, 0] = result
source_file.at[1, 2] = result



# Создание DataFrame с данными
data = {'Header': [result]}
df = pd.DataFrame(data)

# Запись данных в файл Excel
output_file_name = 'Результат от_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.xlsx'
with pd.ExcelWriter(output_file_name) as writer:
    df.to_excel(writer, sheet_name='Sheet1', startrow=1, startcol=0, index=False)

print(f"Данные успешно записаны в файл {output_file_name}")

source_file.to_excel('Na_treni.xlsx', sheet_name='Лист1', index=False)
final_file.to_excel('results1.xlsx', sheet_name='Лист1', index=False)