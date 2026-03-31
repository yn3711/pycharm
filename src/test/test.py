# –– coding: utf-8 –-
"""
サンプル

"""


#--関数の戻り値（返り値）はreturn文で指定する。
def func_return_multi(a, b):
    return a + b, a * b, a / b

#-- []で囲むとタプルではなくリストが返される。

def func_return_multi_list(a, b):
    return [a + b, a * b, a / b]

x = func_return_multi_list(3, 4)

print(x)
print(type(x))

#--戻り値の型は引数および関数の処理に依存する。
x = func_return_multi(3, 4)

print(x)
print(type(x))

#--それぞれの値をアンパックして別々の変数に代入することも可能。
x, y, z = func_return_multi(3, 4)

print(x)
print(y)
print(z)

#--**をつけると複数のキーワード引数が辞書として受け取られる。
def func_kwargs(**kwargs):
    print(kwargs)

func_kwargs(a=1, b=10)

#--
def func_args(*args):
    print(args)

func_args(1, 10)


#--関数呼び出し時にリストやタプルに*をつけて指定すると、要素が展開され順番に位置引数として指定される。要素数と引数の数が一致していないとエラー（TypeError）になる。
def print_add(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('a + b + c = ', a + b + c)

l = [1, 10, 100]

print_add(*l)

#--関数呼び出し時に辞書に**をつけて指定すると、要素のキーが引数名、値が引数の値として展開されてキーワード引数として指定される。引数名と一致するキーが無かったり、一致しないキーがあったりするとエラー（TypeError）になる。

d = {'a': 1, 'b': 10, 'c': 100}

print_add(**d)



#--
def hello():
    print('Hello')

hello()

#--
print("Hello, World")

#--Pythonではコロン（:）とインデント（空白）で繰り返しの制御範囲を表します。Pythonでは「i++」の略記が使えず「i += 1」のみとなります。
n = 0
while n < 10:
    print (n)
    n += 1

"""
Pythonでは「変数宣言」「型宣言」はありません。
最初からそのまま変数に代入できます。
尚、変数の型は代入された値によって自動的に決まります。
"""
a = 2  # 整数
b = 1.23 # 実数
c = "savar" # 文字列
d = 1 + 2j # 複素数
e = True # 論理値
print (c)

"""
for文の書き方は大きく異なります。
Pythonでは、カウント変数iの初期値と終了条件を指定するのにrangeを使います。
range(0, 5, 1)だと初期値は0でカウント数は+1です。
そして、カウント変数が5以下の間、処理を繰り返します。
ただし、カウント変数が+1の場合、range(0, 5)と略記できます。
また、初期値が0ならrange(5)とさらに略記できます。
"""
for i in range(0, 5, 1):
    print(i)


"""
"""
i = 3

if i == 1:
 print("i = 1")
elif i == 2:
 print("i = 2")
elif i == 3:
 print("i = 3")
else:
 print("i = 4")

"""
Pythonには配列に近いものとしてリストがあります。
Pythonでは、print関数に配列を渡すだけで中身を確認できます。
他にもスライスという便利な機能でリストの一部分のみを取り出したり、リストの長さを途中で変更することも可能です。
また、異なるデータ型の要素をもつことができます。
Pythonのリストは自由度が高い一方、要素へ順にアクセスすると処理が重くなるデメリットを抱えています。
そこで、大量のデータを扱う場合は、NumPy配列と呼ばれるC言語の配列に近いものを使います。
ただし、NumPy配列はPython標準機能ではなく、「NumPy」と呼ばれる外部ライブラリを読み込むことで利用できます。
"""
list1 = [1, 2, 3, 4, 5]

print(list1) # [1, 2, 3, 4, 5]
print(list1[1]) # 2


# -*- coding: utf-8
# 異なるデータ型の要素をもてる
list2 = [1, 'two', 3, 'four', 5]

# スライスで2～3番要素のみ取り出して表示
print(list2[2:4]) # [3, 'four']