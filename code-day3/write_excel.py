import requests
import xlsxwriter


TARGET_URL = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=IDR&symbols=USD,CNY"

response = requests.get(TARGET_URL)
data = response.json()['rates']

workbook = xlsxwriter.Workbook('testing.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0, 'Date')
for col, key in enumerate(data[list(data.keys())[0]], start=1):
    worksheet.write(0, col, key)

for row, key in enumerate(data, start=1):
    worksheet.write(row, 0, key)

    for number, kurs in enumerate(data[key]):
        worksheet.write(row, 1+number, round(1/data[key][kurs], 3))

workbook.close()
