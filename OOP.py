class Animal(object):
    def __init__(self,sound,name,age,favorite_color):
            self.sound = sound
            self.name = name
            self.age = age
            self.favorite_color = favorite_color
    def eat(self,food):
            print("Yummy!! " + self.name + " is eating " + food)
    def description(self):
            print(self.name + "is" + self.age +" years old and loves the color "+self.favorite_color)
tamer=Animal("bark","tamer",15,"pink")

            
