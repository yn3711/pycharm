'''
3-13. ポリモーフィズム
　ポリモーフィズム（多態性）は、主にオーバーライドによって実現された子クラスの多様性を指します。例として以下のようなものが挙げられます。
'''

class Animal:
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())