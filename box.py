class Box:
    def __init__(self, *side):
        self.side = side


class Cube(Box):

    def display(self):
        x = self.side[0]
        print("The volume of Cube is : {}".format(x*x*x))


class Cuboid(Box):

    def display(self):
        length = self.side[0]
        width = self.side[1]
        height = self.side[2]
        print("The volume of Cuboid is : {}".format(length*width*height))


class Cylinder(Box):

    def display(self):
        radius = self.side[0]
        height = self.side[1]
        print("The volume of Cuboid is : {}".format(3.14*radius*radius*height))


class Cone(Box):

    def display(self):
        radius = self.side[0]
        height = self.side[1]
        print("The volume of Cuboid is : {}".format(
            (1/3)*3.14*radius*radius*height))


obj1 = Cube(8)
obj1.display()
obj2 = Cuboid(4, 5, 6)
obj2.display()
obj3 = Cylinder(5, 10)
obj3.display()
obj4 = Cone(5, 10)
obj4.display()
