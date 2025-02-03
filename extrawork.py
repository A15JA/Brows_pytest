class Parent:
    def __init__(self):
        print("Parent class initialized")

class Child(Parent):
    def __init__(self):
        print("Child class initialized")
        Parent.__init__(self)  # Manually calling Parent's constructor

# Creating an object of Child
obj = Child()
