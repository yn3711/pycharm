'''

4-4. クラスメンバの継承
　TigerとWhiteTigerを定義し、superの使い方について見ていきます。
superは子クラスの中で親クラスの変数やメソッドを呼び出すための関数です。

return super().eat()は親クラスのeatメソッドを返しているだけで、子クラスの中でeatメソッドを定義しなければsuperを使う必要がありません。
super().__init__(name, age)は、親クラスのイニシャライザ__init__を実行します。
これがないと、self.nameとself.ageを呼び出せません。 super().__init__(name, age)と同等な書き方は以下のようにいくつかあります。
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


class Tiger(Animal):
    def speak(self):
        return "I'm a tiger not Lulu's song"

    def eat(self):
        return "{} is eating".format(self.name)


class WhiteTiger(Tiger):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def speak(self):
        return super().speak().replace("tiger", 'white tiger')

    def eat(self):
        return super().eat()


tony = WhiteTiger("Tony", 10, 100)
print(tony.eat())
# 実行結果：Tony is eating
print(tony.speak())
# 実行結果：I'm a white tiger not Lulu's song


#1. 親クラスの変数を再定義します。

def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height



#2. 親クラスの__init__を明示的に呼び出します。親クラスの名前を変えると、呼び出された箇所を全部修正しなければなりません。

def __init__(self, name, age, height):
    Tiger.__init__(self, name, age)
    self.height = height