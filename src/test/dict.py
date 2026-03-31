#
pair = [['a', 'b'],['c', 'd'],['e', 'f']]
print(dict(pair))

#2つのリストでzip関数を使った例
x = [1, 2, 3]
y = [4, 5, 6]
for num in zip(x, y):
  print(num)

#タプルの場合もリストと同じ結果になります。
x = (1, 2, 3)
y = (4, 5, 6)
for num in zip(x, y):
  print(num)


#for in文の中の変数をイテラブルなオブジェクトの数に合わせると、それぞれの変数に値が入ります
y = [4, 5, 6]
for num_x, num_y in zip(x, y):
  print('num_x:', num_x, 'num_y:', num_y)
  print('------------------')
