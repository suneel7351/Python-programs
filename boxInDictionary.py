import math
from math import pi



def CubeVolume(side):
    return side*side*side


def CubeArea(side):
    return 6*side*side


def CuboidVolume(length, width, height):
    return length*width*height


def CuboidArea(length, width, height):
    return 2 * (length * width + length * height + width * height)


def ConeVolume(radius, height):
    return (1/3) * math.pi * radius * radius * height


def ConeArea(radius, slant_height):
    return math.pi * radius * slant_height + pi * radius * radius


Box = {
    "cube": {
        "volume": CubeVolume,
        "area": CubeArea
    },
    "Cuboid": {

        'volume': CuboidVolume,
        'area': CuboidArea
    },
    "Cone": {

        'volume': ConeVolume,
        'area': ConeArea
    }
}

print("Volume of Cube is : {}".format(Box['cube']['volume'](2)))
print("Area of Cube is : {}".format(Box['cube']['area'](2)))
print("Volume of Cuboid is : {}".format(Box['Cuboid']['volume'](4, 5, 6)))
print("Area of Cuboid is : {}".format(Box['Cuboid']['area'](4, 5, 6)))
print("Volume of cone is : {}".format(Box['Cone']['volume'](4, 5)))
print("Area of cone is : {}".format(Box['Cone']['area'](4, 5)))
