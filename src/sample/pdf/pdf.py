# ライブラリを読み込み
import win32com.client
import os

# 読み込み元ファイルと書き込み先を指定する
base = os.path.dirname(__file__)
input_file = os.path.join(base, "../excel/demo.xlsx")
output_file = os.path.join(base, "output.pdf")

# Excelを起動する
app = win32com.client.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelでワークブックを読み込む
book = app.Workbooks.Open(input_file)
# PDF形式で保存
xlTypePDF = 0
book.ExportAsFixedFormat(xlTypePDF, output_file)

# Excelを終了
app.Quit()