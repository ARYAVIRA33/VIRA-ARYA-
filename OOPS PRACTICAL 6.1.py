# Python program to show multiple inheritance
class Base1:
    def __init__(self):
        self.string_1 = "Hi"
        print("Base 1: ")


class Base2(object):
    def __init__(self):
        self.string_2 = "Hello"
        print("Base 2: ")


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)        # Calling constructors of Base1 class
        Base2.__init__(self)        # Calling constructors of Base1 class
        print("Derived: ")

    def print_strings(self):
        print(self.string_1, self.string_2)


object_ = Derived()
object_.print_strings()

# Output : Base 1, Base 2, Derived(Hi, Hello)
