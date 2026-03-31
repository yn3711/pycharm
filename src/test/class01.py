'''
https://qiita.com/kaitolucifer/items/926ed9bc08426ad8e835#
https://techacademy.jp/magazine/27996

継承」、「カプセル化」、「ポルモーフィズム」
4-1. クラスの変数とメソッド
　Pythonのクラスには変数とメソッドがあります。そして、それぞれ色々な種類があります。

変数は
  クラス変数とインスタンス変数があります。
メソッドは
  クラスメソッド、
  インスタンスメソッド、
  静的メソッドがあります。

クラス変数は
  クラスが持つ変数で、クラスとインスタンス両方で使えます。
  インスタンスメソッドからクラス変数にアクセスするには、クラス.変数名とすればよい。
  selfでアクセスする場合、クラス変数が不変(読み込みのみ)の場合は特に問題ない。
  (注:PythonはJavaでいうfinalに相当する機能がないため、あくまで書き変えをしないで扱いましょうという紳士協定)
  しかしクラス変数を可変にしたい場合、気をつけないと「クラス変数を書き変えたつもりが同名のインスタンス変数を定義した」ということが起こりうる。

インスタンス変数は
  各インスタンスに所属するもので、そのインスタンスのみ使用できます。


インスタンスメソッドは
  インスタンスが使うメソッドで、selfというインスタンス自身を指す引数を定義する必要があります。

クラスメソッドは
  クラスとインスタンス両方が使えるメソッドで、clsというクラスを指す引数を定義する必要があります。

静的メソッドは
  クラス内部で管理する普通の関数で、クラスとインスタンス両方が使えます。

クラスからクラス変数を修正すると、インスタンスから呼び出す時に変更されます。
インスタンスからクラス変数を修正すると、他のクラスやインスタンスに影響を与えません。
メソッドのモンキーパッチはMethodTypeか直接代入で実現できます。
インスタンスにメソッドをバインディングすると、元のクラスや他のインスタンスはバインディングされたメソッドが使えません。
クラスににバインディングすると、全てのインスタンス（バインディングする前に作成したインスタンスも含む）に伝播します。
'''

from types import MethodType


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

    #　静的メソッドはインスタンス化しなくても、呼び出せるメソッドのことを指します。
    @staticmethod
    def happening(person, do):  # 静的メソッド
        print("{} is {}ing".format(person, do))


def drink_water(self):
    print("{} is drinking water".format(self.name))


adam = Animal(name="Adam", age=2)  # インスタンス化
print('adam.the_name: {}'.format(adam.the_name))  # インスタンスからクラス変数を呼び出す
# 実行結果：adam.the_name: animal
print('Animal.the_name: {}'.format(Animal.the_name))  # クラスからクラス変数を呼び出す
# 実行結果：adam.name: Adam
print('adam.name: {}'.format(adam.name))  # インスタンス変数を呼び出す
# 実行結果：Animal.the_name: animal
adam.sleep()  # インスタンスメソッドを呼び出す
# 実行結果：Adam is sleeping
adam.eat("meat")  # 引数付きのインスタンスメソッドを呼び出す
# 実行結果：Adam is eating meat
adam.speak("happy")  # インスタンスからクラスメソッドを呼び出す
# 実行結果：I am a happy animal
Animal.speak("sad")  # クラスからクラスメソッドを呼び出す
# 実行結果：I am a sad animal
adam.happening("Tim", "play")  # インスタンスから静的メソッドを呼び出す
# 実行結果：Tim is playing
Animal.happening("Mary", "watch")  # クラスから静的メソッドを呼び出す
# 実行結果：Mary is watching
Animal.the_name = "Animal"  # クラス変数を修正
print('adam.the_name: {}'.format(adam.the_name))
# 実行結果：adam.the_name: Animal
adam.the_name = "animal"  # インスタンスから修正
print('Animal.the_name: {}'.format(Animal.the_name))
# 実行結果：Animal.the_name: Animal
adam.age = 3  # インスタンス変数を修正

# メソッドのバインディング（モンキーパッチ）
adam.drink_water = MethodType(drink_water, adam)  # インスタンスにバインディングする
adam.drink_water()
# 実行結果：Adam is drinking water
print(adam.drink_water)
# 実行結果：<bound method drink_water of <__main__.Animal object at 0x7ffd68064310>>
try:
    Animal.drink_water
except AttributeError as e:
    print(e)
# 実行結果：type object 'Animal' has no attribute 'drink_water'
Animal.drink_water = MethodType(drink_water, Animal)  # クラスにバインディングする
adam.drink_water()
# 実行結果：Adam is drinking water
Animal.drink_water = drink_water  # 直接代入でメソッドをバインディングする
adam.drink_water()
# 実行結果：Adam is drinking water

