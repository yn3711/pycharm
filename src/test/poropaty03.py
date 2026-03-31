class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # @propertyとすると、nameプロパティのgetterとして定義できる
    def name(self):
        print("getterを呼び出しました")
        return self.__name
        ##↑privateの変数、__nameを返す

    @property
    def age(self):
        return self.__age

    @name.setter  # nameプロパティのsetterとして定義する。
    def name(self, value):
        print("setterを呼び出しました")
        self.__name = value
        ##↑ privateの変数、__nameを設定する

    @age.setter
    def age(self, value):
        self.__age = value

    @name.deleter  # nameプロパティのdeleterとして定義される。
    def name(self):
        print("deleterを呼び出しました")
        del self.__name

    @age.deleter
    def age(self):
        del self.__age


man = Human("Taro", 20)
print(man.name)
##↑ man.nameとするとnameのsetterが呼び出され、__nameが表示される
##"getterを呼び出しました"
##と表示される

man.name = "PP"
##↑ man.name = ""
##とするとnameのgetterが呼び出され、__nameの値が変更される
##"##setterを呼び出しました"
##と表示される

del man.name
##↑ del man.nameとするとnameのdeleterが呼び出され、__nameが表示削除される
##"detterを呼び出しました"
##と表示される