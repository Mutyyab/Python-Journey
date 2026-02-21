import openpyxl as xl
Book = xl.load_workbook('Book1.xlsx')
Sheet1 = Book['Sheet1']
Cell = Sheet1.cell(row=1, column=1)
for row in range(2,Sheet1.max_row+1):
     cell = Sheet1.cell(row=row, column=3)
     corrected_price = cell.value*0.9
     corrected_price_cell = Sheet1.cell(row=row, column=4)
     corrected_price_cell.value = corrected_price

Book.save('Book2.xlsx')