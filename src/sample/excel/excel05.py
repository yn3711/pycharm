'''
https://qiita.com/github-nakasho/items/fb9df8e423bb8784cbbd
    sheet_copy.py
    purpose: make new xlsx and copy sheet
    Pythonのコード例を以下に示します。以下の例ではfgo.xlsxのシート1の内容を読み込み、新規作成したfgo_2.xlsxのclassというシートにコピーしています
'''

import openpyxl as xl


# set input file name
##inputfile = '../torihiki.xlsx'
inputfile = 'torihiki.xlsx'

# set output file name
##outfile = '../demo.xlsx'
outfile = 'demo.xlsx'

# set output sheet title
sheettitle = 'Sheet1'

# read tmp xlsx
wb1 = xl.load_workbook(filename=inputfile)
ws1 = wb1.worksheets[0]

# create new xlsx file
wb2 = xl.Workbook()
ws2 = wb2.worksheets[0]
ws2.title = sheettitle

# write to sheet in output file
for row in ws1:
    for cell in row:
        ws2[cell.coordinate].value = cell.value

# save target xlsx file
wb2.save(outfile)