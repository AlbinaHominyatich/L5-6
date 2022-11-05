class Grandparent:
    height = 160
    age = 60
    satiety = 100
class Parent(Grandparent):
    age = 40
class Child(Parent):
    height = 170
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
sasha = Child()
