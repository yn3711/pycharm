import copy

class Foo(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
    def copy(self):
        return copy.deepcopy(self)

a = Foo()
a.x = 1
a.y = 2
a.z = 3
print(a)

b = a.copy()
b.x = 2
print(a.x)
print(b.x)
print(b)

c = a.copy()
c.x = 3
print(a.x)
print(b.x)
print(c.x)
print(c)

d = [0 for i in range(10)]

d[0] = a.copy()
d[0].x = 4
print(a.x)
print(b.x)
print(c.x)
print(d[0].x)
print(d)

d[1] = a.copy()
d[1].x = 5
print(a.x)
print(b.x)
print(c.x)
print(d[1].x)
print(d)