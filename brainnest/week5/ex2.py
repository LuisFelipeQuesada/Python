# Inheritance: Create a subclass called Student that inherits from the Person class.
# Add a new attribute called university to the Student class and initialize it in the constructor.
# Also, override the introduce() method to include information about the student's university.
class Person:

    __name = ""

    def __init__(self, name):
        self.__name = name

    def introduce(self):
        return f"Hello, I'm {self.__name}"
    
    def greet(self):
        return "Nice to meet you"

class Student(Person):

    __university = ""

    def __init__(self, name):
        super().__init__(name)
        self.__university = "Johns Hopkins"

    def introduce(self):
        return f"I study at the {self.__university} university"
    
s = Student("Emilia")
print(s.greet())
print(s.introduce())