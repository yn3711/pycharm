'''
2-2. カプセル化
　オブジェクト指向は関数とデータを一緒に束ねてくれるので、同じ変数（データ）をたくさんの関数で処理したい時はとても便利です。
'''


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def describe(self):
        print("name: {}; age: {}; height: {}".format(self.name, self.age, self.height))

    def introduce(self):
        print("My name is {}, and height is {}, and age is {}. ".format(self.name, self.height, self.age))


bob = Person("Bob", 24, 170)
mary = Person("Mary", 10, 160)
bob.describe()
bob.introduce()
mary.describe()
mary.introduce()

'''
引数を辞書で格納して、引数として辞書をアンパックして渡すようにしています。
しかし、もし辞書の中にname, age, heightの3つのキーが存在しないと、エラーを起こしてしまいます。
'''

bob = dict(name='Bob', age=24, height=170)
mary = dict(name='Mary', age=20, height=160)


def introduce(**kwargs):
    print("My name is {name}, and height is {age}, and age is {height}. ".format(**kwargs))


def describe(**kwargs):
    print("Description: name is {name}, age is {age}, height is {height}".format(**kwargs))


introduce(**bob)
describe(**bob)
introduce(**mary)
describe(**mary)