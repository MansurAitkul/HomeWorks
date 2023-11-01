import openpyxl

file_path = "путь_к_вашему_файлу.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active
total_sum = 0

for row in sheet.iter_rows(values_only=True):
    for cell_value in row:
        if isinstance(cell_value, (int, float)):
            total_sum += cell_value

print(f"Общая сумма числовых данных: {total_sum}")
