import os
import csv

stores_path = "店舗コード.csv"

with open(stores_path, encoding="cp932") as f:
    reader = csv.reader(f)
    for row in reader:
        folder_name = row[0] + '_' + row[1]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
