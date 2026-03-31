
'''
4-2. プロパティ
　Animalを継承したDogクラスを作成し、propertyやそれに関連するデコレーターを見てみます。これらのデコレーターはメソッドをプロパティ（変数）に変換するもので、以下の2つのメリットがあります。

インスタンス変数のように()なしで呼び出せます。
変数の評価機能などの動的な処理を追加でき、合法性を保証できます。
　デコレーター以外に、property関数で上記の処理を実現できる方法もあります。

@propertyデコレーターはメソッドを変数に変換します。
property関数でも同じ処理を実現できます。4番目の引数"I'm the 'city' property."という文字列はドキュメントで、Dog.city.__doc__で確認できます。
@cached_propertyはPython 3.8で実装された値がキャッシュされるpropertyです。計算量の高い変数処理をする時、キャッシュされると再計算が必要なくなるので性能向上に繋がります。

'''

from functools import cached_property

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

class Dog(Animal):  # クラスの継承
    def eating(self):
        print("{} is eating".format(self.name))

    @property
    def running(self):
        if self.age >= 3 and self.age < 130:
            print("{} is running".format(self.name))
        elif self.age > 0 and self.age < 3:
            print("{} can't run".format(self.name))
        else:
            print("please input true age")

    @property  # プライベートな変数を取得する
    def country(self):
        return self._country

    @country.setter  # メソッド名.setter
    def country(self, value):  # プライベートな変数に値を代入する
        self._country = value

    @country.deleter  # メソッド名.deleter
    def country(self):  # プライベートな変数に値を削除する
        del self._country
        print("The attr country is deleted")

    # property関数で上記のデコレーターと同じ機能を実現
    def get_city(self):
        return self._city

    def set_city(self, value):
        self._city = value

    def del_city(self, value):
        del self._city

    city = property(get_city, set_city, del_city, "I'm the 'city' property.")

    @cached_property  # キャッシュされるproperty
    def official_name(self):
        return 'Mr.{} - the Dog'.format(self.name)


david = Dog("David", 2)
david.eating()
# 実行結果：David is eating
david.running  # ()なしで呼び出す
# 実行結果：David can't run
dean = Dog("Dean", 4)
dean.running
# 実行結果：Dean is running

# デコレーターによる方法
david.country = "America"
print(david.country)
# 実行結果：America
del david.country
# 実行結果：The attr country is deleted

# property関数による方法
david.city = "NewYork"
print(david.city)
# 実行結果：NewYork

# キャッシュされるproperty
print(david.official_name)
# 実行結果：Mr.David - the Dog