# class ParentClass:
#     def speak(self):
#         print("Jestem rodzicem.")

# class ChildClass(ParentClass):
#     def speak(self):
#         super().speak()
#         print("Jestem dzieckiem.")

# child = ChildClass()
# child.speak()


# def area(shape):
#     return shape.calculate_area()

# class Circle:
#     def __init__(self, radious):
#         self.radious = radious

#     def calculate_area(self):
#         return 3.14 * self.radious
    
# class Recrangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.height * self.width


# circle = Circle(5)
# rectangle = Recrangle(4,3)
# print("Pole Koła:", area(circle))
# print("Pole prostokąta:", area(rectangle))



# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Hau!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Miau!"
    
# def make_animal_speak(animal):
#     return animal.speak()

# dog = Dog()
# cat = Cat()

# print(make_animal_speak(dog))
# print(make_animal_speak(cat))

                                    #co to dziedziczenie klas?


#klasy abstrakcyjne

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radious):
#         self.radious = radious

#     def calculate_area(self):
#         return 3.14 * self.radious
    
# class Recrangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.height * self.width

# # abc = Shape() nie można
# circle = Circle(5)
# rectangle = Recrangle(4,3)
# print("Pole Koła:", circle.calculate_area())
# print("Pole prostokąta:", rectangle.calculate_area())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"{self.name}, {self.age} lat"
    
person = Person("Alicja", 33)
print(str(person))



#zmienne prywatne i silnie prywatne