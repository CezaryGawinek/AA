def my_decorator(func):
    def wrapper():
        print("tekst przed funkcja")
        func()
        print("teskt po funkcji")
    return wrapper()

@my_decorator
def czesc():
    print("hello")
    

# class Person:
#     def __init__(self, name):
#         self.name = name 

# person = Person("Jon")
# person.wiek = 30    #atrybut dynamiczny

# print(person.wiek)

# class Circle:
#     def __init__(self, radious):
#         self.radious = radious

#     def calculate(self): 
#         return 3.14 * self.radious**2

# circle = Circle(10)
# pole = circle.calculate()
# print(pole)
# circle.radious=4
# pole=circle.calculate()

# class Kwadrat:
#     #atrybuty
#     width = 0
#     height = 0

#     def __init__(self, width, height):
#         self.width = width
#         self. height = height

#     @classmethod #dekorator - nie trzeba uruchamiać klasy 
#     def pole_kwadratu(cls, atrubuty): #cls = wszystkie atrybuty tu wejdą (width, height)
#         return cls(atrubuty, atrubuty)
    

#     @staticmethod
#     def obwod(a,b):
#         return a*2+b*2
    
#     def __add__(self, ):
#         return self.height + self.width
    

# pole = Kwadrat.pole_kwadratu(4)
# print(pole.height)
# print(Kwadrat.obwod(4,6))




# class Car:
#     # atrybuty klasy
#     kolor = "Czerwony"
#     def __init__(self, make, model, year):   #metoda inicjacyjna
#         #atrybuty instancji
#         self.make = make
#         self.model = model
#         self.__year = year   #

#     def get_year(self):
#         return self.__year
#     def set_year(self,new__year):
#         self.__year = new__year

# car = Car("Toyota", "Camry", 2023)
# print(car.get_year())
# car.set_year(2020)
# print(car.get_year())
# print(car.kolor)
# car.kolor = "Zielony"
# print(car.kolor)
