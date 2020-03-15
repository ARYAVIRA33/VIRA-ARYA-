import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_result(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, another_circle):
        return Circle(self.radius + another_circle.radius)

    def __sub__(self, another_circle):
        return Circle(self.radius - another_circle.radius)

    def __mul__(self, another_circle):
        return Circle(self.radius * another_circle.radius)

    def __gt__(self, another_circle):
        return Circle(self.radius > another_circle.radius)

    def __lt__(self, another_circle):
        return Circle(self.radius < another_circle.radius)

    def __ge__(self, another_circle):
        return Circle(self.radius >= another_circle.radius)

    def __le__(self, another_circle):
        return Circle(self.radius <= another_circle.radius)

    def __eq__(self, another_circle):
        return Circle(self.radius == another_circle.radius)

    def __ne__(self, another_circle):
        return Circle(self.radius != another_circle.radius)


c1 = Circle(10)
print(c1.get_result())
print(c1.area())

c2 = Circle(15)
print(c2.get_result())
print(c1.area())

c3 = c1 + c2
print(c3.get_result())

c3 = c2 - c1
print(c3.get_result())

c4 = c1 * c2
print(c4.get_result())

c5 = c1 < c2
print(c5.get_result())

c5 = c2 < c1
print(c5.get_result())
