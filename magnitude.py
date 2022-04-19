import math


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        i = self.x
        j = self.y
        return math.sqrt(math.pow(i, 2) + math.pow(j, 2))


obj = Complex(6, 8)
print(obj.magnitude())
