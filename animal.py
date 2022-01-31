class Animal(object):
    def __init__(self, name, speed, family, subfamily, lifespan):
        self.name = name,
        self.speed = speed,
        self.family = family,
        self.subfamily = subfamily,
        self.lifespan = lifespan

    def display(self):
        print("Name : ", (self.name[0]))
        print("speed : ", (self.speed)[0])
        print("family : ", (self.family)[0])
        print("subfamily : ", (self.subfamily)[0])
        print("lifespan : ", (self.lifespan))


animal = [

    Animal("lion", 80, "falidae", "pantherinae", 12),
    Animal("tiger", 65, "falidae", "pantherinae", 10),
    Animal("elephant", 30, "Elephantidae", "Elephantoidea", 48),
    Animal("cat", 48, "falidae", "falinae", 15),
]

for x in animal:
    print(x.display())
