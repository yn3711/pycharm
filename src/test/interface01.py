from src.test.interface import  Abstract  #from モジュール名 import スーパークラス名

class Implement(Abstract):
    @classmethod
    def uppercase01(cls, name):
        return name.upper() + ' by Impl'

Implement('Dan')