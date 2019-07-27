import xlrd


workbook = xlrd.open_workbook("testing.xlsx")
worksheet = workbook.sheet_by_index(0)

row = 0

while True:
    try:
        data = [worksheet.cell_value(row, i) for i in range(3)]
    except:
        break
    print(data)
    row+=1
