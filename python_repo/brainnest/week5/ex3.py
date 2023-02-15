# 3. Polymorphism: Define a class Pet with an attribute called name and a method speak().
# Create two subclasses Dog and Cat that inherit from the Pet class. Override the speak() method in the Dog and Cat
# classes to return a string that is specific to each type of pet.

class Pet:

    __name = ""

    def __init__(self, name):
        self.__name = name
    
    def speak(self):
        return f"Hello, I'm {self.__name}"

class Dog(Pet):

    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return "Guau guau"

class Cat(Pet):

    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return "Miau miau"

p = Pet("Freya")
print(p.speak())

d = Dog("Thor")
print(d.speak())

c = Cat("Baldr")
print(c.speak())

