'''
4-3. プライベート変数とメソッドの継承・オーバーライド
　Catクラスとその子クラスBlackCatを定義し、プライベート変数とメソッドの継承・オーバーライドについて見ていきます。

プライベートな変数は外部から使うことが制限される変数です。
子クラスは親クラスを継承する時、親クラスのメソッドを全部継承しますが、子クラスの中で同じ名前のメソッドを定義すると、継承されたメソッドがオーバーライドされます。
イニシャライザメソッドの__init__も同様です。

weightは普通の変数で、外部から利用できます。
_weightのような1つのアンダースコアが付いてる変数は外部からの利用を推奨しないプライベート変数で、利用すること自体は制限されません。
ただし、オブジェクト名（クラス名、関数名、モジュールスコープの変数名など）にする場合、from module import *ではimportされません。
__weightのような2つのアンダースコアが付いてる変数は外部からの利用を禁止するプライベート変数です。
ただし、<class>._<class>__xの形で強制的に呼び出せます。継承による属性の衝突を避けたい場合に使用するべきです。
変数名のパターンによる違う動作の実現は「名前修飾（Name Mangling）」と言います。
子クラスの中で親クラスが持っているメソッドと同じ名前のメソッドを定義すると、オーバーライドすることができます。
4-4. クラスメンバの継


'''
class Animal:
    # ここはクラス変数を定義する場所
    the_name = "animal"  # クラス変数

    def __init__(self, name, age):  # イニシャライザ
        self.name = name  # インスタンス変数
        self.age = age

    # ここはメソッドを定義する場所
    def sleep(self):  # インスタンスメソッド
        print("{} is sleeping".format(self.name))

    def eat(self, food):  # 引数付きのインスタンスメソッド
        print("{} is eating {}".format(self.name, food))

    @classmethod
    def speak(cls, adjective):  # クラスメソッド
        print("I am a {} {}".format(adjective, cls.the_name))

    @staticmethod
    def happening(person, do):  # 静的メソッド
        print("{} is {}ing".format(person, do))

class Cat(Animal):
    def __init__(self, weight):  # 親クラスの__init__をオーバーライド
        self.__weight = weight
        self._weight = weight + 1
        self.weight = self._weight + 1

    def get_weight(self):
        print("My _weight is {}kg".format(self._weight))

    def get_real_weight(self):
        print("Actually my __weight is {}kg".format(self.__weight))


class BlackCat(Cat):
    def get_weight(self):  # 親クラスのメソッドをオーバーライド
        print("My weight is {}kg".format(self.weight))

    def get_real_weight(self):
        print("Actually my _weight is {}kg".format(self._weight))

    def get_actual_weight(self):
        print("My __weight is exactly {}kg".format(self.__weight))

cole = Cat(5)
print("Cole's weight: {}kg".format(cole.weight))
# 実行結果：Cole's weight: 7kg

# _xは外部からの利用を推奨しないプライベート変数で、利用すること自体は制限されない
print("Cole's _weight: {}kg".format(cole._weight))
# 実行結果：Cole's _weight: 6kg

# __xは外部からの利用をを禁止するプライベート変数で、利用することは制限され、_<class>__xの形で強制的に呼び出せる
print("Cole's __weight: {}kg".format(cole._Cat__weight))
# 実行結果：Cole's __weight: 5kg
cole.get_real_weight()  # メソッドで内部から__xを利用できる
# 実行結果：Actually my __weight is 5kg

cain = BlackCat(5)
cain.get_weight()
# 実行結果：My weight is 7kg

# _xは制限されないため、子クラスからでも呼び出せる
cain.get_real_weight()
# 実行結果：Actually my _weight is 6kg

# 親クラスのプライベート変数の__xを子クラスの内部から素直な方法では利用できない
try:
    cain.get_actual_weight()
except AttributeError as e:
    print(e)
# 実行結果：'Blackcat' object has no attribute '_Blackcat__weight'