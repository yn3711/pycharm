class User:

    def __init__(self, name):
        self.name = name
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if type(age) == int:
            if age > 0:
                self.__age = age
                return

        raise ValuError('年齢は0以上の整数を指定してください')
