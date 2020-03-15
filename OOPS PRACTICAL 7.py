import math
# Super class


class Polygons:
    def number_of_sides(self):
        return 0

    def area(self):
        return 0

    def perimeter(self):
        return 0


# Triangle class inherits from Polygons
class Triangle(Polygons):
    def number_of_sides(self):
        return 3

    def area(self, base, height):
        return 1 / 2 * base * height

    def perimeter(self, a, b, c):
        if a + b > c:
            return a + b + c
        else:
            return "Invalid input: make sure a + b > c"


# Rhombus class inherits from Polygons
class Rhombus(Polygons):

    def number_of_sides(self):
        return 4

    def area(self, p, q):
        return p * q / 2

    def perimeter(self, a):
        return 4 * a


# Pentagon class inherits from Polygons
class Pentagon(Polygons):
    def number_of_sides(self):
        return 5

    def area(self, a):
        return 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2

    def perimeter(self, a):
        return 5 * a


# Hexagon class inherits from Polygons
class Hexagon(Polygons):
    def number_of_sides(self):
        return 6

    def area(self, a):
        return (3 * math.sqrt(3) / 2) * a ** 2

    def perimeter(self, a):
        return 6 * a

# Below is some test cases.
tri = Triangle()
print("Triangle Area:", tri.area(15, 25))
print("Perimeter:", tri.perimeter(15, 20, 25))
print("-----------------")
rho = Rhombus()
print("Rhombus Area:", rho.area(15, 25))
print("Perimeter:", rho.perimeter(30))
print("-----------------")
pent = Pentagon()
print("Pentagon Area:", pent.area(15))
print("Perimeter:", pent.perimeter(25))
print("-----------------")
hex = Hexagon()
print("Hexagon Area:", hex.area(15))
print("Perimeter:", hex.perimeter(25))
print("-----------------")
