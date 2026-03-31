# win32com ライブラリを読み込み
import win32com.client

# Excelを起動する
app = win32com.client.Dispatch("Excel.Application")
app.Visible = True

# Excelに新規ワークブックを追加
book = app.Workbooks.Add()

# アクティブなシートを得る
sheet = book.ActiveSheet
# シートに値を書き込む
sheet.Range("B2").Value = "こんにちは"