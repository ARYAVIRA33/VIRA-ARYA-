class shapes:
    def __init__(self, square, rectangle):
        self.square = square
        self.rectangle = rectangle

    def display(self):
        print("square", self.square)
        print("rectangle", self.rectangle)
side = int(input("enter the side  "))
length = int(input("enter the length  "))
breath = int(input("enter the breath  "))
square = side*side
rectangle = length*breath

s1 = shapes(square, rectangle)
s1.display()
