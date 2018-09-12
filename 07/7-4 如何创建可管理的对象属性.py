import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return round(self.radius, 1)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('wronge type')
        self.radius = radius

    @property
    def S(self):
        return self.radius ** 2 * math.pi

    @S.setter
    def S(self, s):
        self.radius = math.sqrt(s / math.pi)

    R = property(get_radius, set_radius)

c = Circle(5.712)

c.S = 99.88
print(c.S)
print(c.R)

#print(c.get_radius())
#c.radius = '31.98'

