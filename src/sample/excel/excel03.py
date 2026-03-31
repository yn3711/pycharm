# xlsheet_read_to_dict.py
import openpyxl

# エクセルファイルの取り込み
wb = openpyxl.load_workbook("torihiki.xlsx")
ws = wb["Sheet1"]

# 学生リスト
student_list = []
# 列名のセル
header_cells = None

for row in ws.rows:
    if row[0].row == 1:
        # 1行目
        header_cells = row
    else:
        # 2行目以降
        row_dic = {}
        # セルの値を「key-value」で登録
        for k, v in zip(header_cells, row):
            row_dic[k.value] = v.value
        student_list.append(row_dic)

print(student_list)