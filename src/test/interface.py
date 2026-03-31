## https://qiita.com/ukisoft/items/b7c410b96dde1922a2d0

from abc import ABCMeta, abstractmethod

class Abstract(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @classmethod
    @abstractmethod
    def uppercase(cls, name):
        raise NotImplementedError()

    def explain(self):
        print(self.name)

    @abstractmethod
    def hello(self):
        raise NotImplementedError()


class Implement(Abstract):
    @classmethod
    def uppercase(cls, name):
        return name.upper() + ' by Impl'

#abs = Abstract('Bob')

