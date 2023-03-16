import openpyxl
wb = openpyxl.Workbook()

import openpyxl
wb = openpyxl.Workbook()
hoja = wb.active
print(f'Hoja activa: {hoja.title}')
Hoja activa: Productos
hoja.title = "Productos"
print(f'Hoja activa: {wb.active.title}')
Hoja activa: Productos