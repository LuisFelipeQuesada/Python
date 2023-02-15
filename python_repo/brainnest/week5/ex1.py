# 1. Create methods in a class:
# In the Person class, add methods like introduce() and greet().
# The introduce() method should print a brief introduction about the person and the greet()
# method should print a friendly greeting.
class Person:

    __name = ""

    def __init__(self, name):
        self.__name = name

    def introduce(self):
        return f"Hello, I'm {self.__name}"
    
    def greet(self):
        return "Nice to meet you"

p = Person("Ana")
print(p.introduce())
print(p.greet())