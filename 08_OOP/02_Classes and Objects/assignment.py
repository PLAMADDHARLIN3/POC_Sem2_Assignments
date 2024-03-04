from math import hypot, atan, degrees, pi

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.min_angle = atan(self)

        def area(self): 