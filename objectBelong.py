class A:
    pass


class B:
    pass


class C:
    pass


obj1 = A()
obj2 = B()
obj3 = C()

x = type(obj1)
y = type(obj2)
z = type(obj3)
print(x.__name__)
print(y.__name__)
print(z.__name__)
