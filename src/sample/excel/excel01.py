import openpyxl

# ワークブックを新規作成する
book = openpyxl.Workbook()

# シートを取得し名前を変更する
sheet = book.active
sheet.title = 'First sheet'

# 範囲を指定してセルを取得する
cells = sheet['A1':'B3']
i = 0
for row in cells:
    for cell in row:
        cell.value = i # セルに値を設定する
        i += 1

# ワークブックに名前をつけて保存する
#book.save('../demo.xlsx')
book.save('demo.xlsx')