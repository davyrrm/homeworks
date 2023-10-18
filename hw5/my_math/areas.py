import math
import warnings

if __name__ == '__main__':
    warnings.warn("См. main module.", UserWarning)

def rectangle_area(length, breadth):
    return length * breadth

def square_area(side):
    return side * side

def triangle_area(base, height):
    return 0.5 * base * height

def sphere_area(radius):
    return 4 * math.pi * radius ** 2
