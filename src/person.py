class Person:

    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def grow_older(self):
        self.age += 1

    def set_height(self,height):
        self.height = height

    def set_weight(self,weight):
        self.weight = weight

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old"
