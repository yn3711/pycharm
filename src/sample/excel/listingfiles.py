import os
import csv
import time

csv_file = 'filelist.csv'
date_format = '%Y/%m/%d %H:%M:%S'

file_list = []

for file in os.listdir("../../.."):
    # ファイルかどうか
    is_file = os.path.isfile(file)
    # このpyファイル自身でないか
    not_py_file = os.path.basename(__file__) != file
    # リストCSVファイルでないか
    not_csv_file = csv_file != file

    if is_file and not_py_file and not_csv_file:
        # ファイル作成時刻
        time_crt = time.strftime(date_format,
                                 time.localtime(os.path.getctime(file)))
        # ファイル更新時刻
        time_mod = time.strftime(date_format,
                                 time.localtime(os.path.getmtime(file)))

        file_list.append([file, time_crt, time_mod])

with open(csv_file, "w", newline="") as f:
    csv_writer = csv.writer(f)
    for r in file_list:
        csv_writer.writerow(r)