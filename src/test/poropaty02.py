##https://www.nblog09.com/w/2019/01/09/python-setter-getter/

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):  # __nameのgetterの定義
        print("getterを呼び出しました")
        return self.__name
        # ↑private変数の__nameを返す。

    def get_age(self):
        return self.__age

    def set_name(self, value):  # __nameのsetterの定義
        print("setterを呼び出しました")
        self.__name = value
        # ↑private変数の__nameを設定します。

    def set_age(self, value):
        self.__age = value

    name = property(get_name, set_name)
    ##property関数を利用することで、get_nameとset_nameを呼び出す機能を持ったnameプロパティが作成されます。
    age = property(get_age, set_age)


man = Human("Taro", 23)
print(man.name)
##↑ man.nameとすると、get_nameが呼び出され、"getterを呼び出しました"
##と表示されます。
man.name = "Jiro"
##↑ man.name = とすると、set_nameが呼び出され、"setterを呼び出しました"
##と表示されます。
print(man.name)
##Jiroと表示
print(man.age)
##23
##と表示