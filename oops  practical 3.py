class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print("name", self.name)
        print("roll no", self.rollno)

name = str(input("enter name:"))
rollno = int(input("enter rollno"))
#s = student(name, rollno)
student(name,rollno).display()
