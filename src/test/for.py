# –– coding: utf-8 –-
"""
 サンプル
 for
 https://gammasoft.jp/blog/read-rows-of-excel-sheet-using-python/
"""


#-- 添え字指定
l = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for c in l[2:5]:
 print(c)

#--for文の途中で処理を終了したい場合はbreakを使う。
l = ['Alice', 'Bob', 'Charlie']
for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)


#--
l = ['Alice', 'Bob', 'Charlie']
for name in l:
    print(name)