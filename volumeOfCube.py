class Cube:
    def __init__(self, side):
        self.side = side

    def volume(self):
        x = self.side
        print("Volume of cube is " + str(x*x*x))


vol = Cube(3)
vol.volume()
