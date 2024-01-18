#python -m venv car - tworzy wirtualne srodowicho
#pierwsza klasa o aucie
#modyfikacja

import logging

logging.basicConfig(filename="car.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class Car:
    def __init__(self, make, model, year):
        self.__make = make  #ukryty
        self.__model = model
        self.__year = year
        self.__is_production = False 

    def start_production(self):
        if not self.__is_production:
            logging.info(f"Rozpoczecie produkcji {self.__make} {self.__model} {self.__year}")
            self.__is_production = True
        else:
            logging.warning("Aktualnie jest produkowany")

    def stop_production(self):
        if self.__is_production:
            logging.info(f"Zatrzymanie produkcji {self.__make} {self.__model} {self.__year}")
            self.__is_production = False
        else:
            logging.warning("Aktualnie nie jest produkowany")
    
    def display_info(self):
        logging.info(f"Marka: {self.__make}")
        logging.info(f"Model: {self.__model}")
        logging.info(f"Rocznik: {self.__year}")
        logging.info(f"Czy jest aktualnie produkcja? {'Tak' if self.__is_production else 'Nie'}")

class ElectricalCar(Car): #z nawiasem przyjmuje parametry klasy Car
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.__battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        logging.info(f"Pojemność baterii: {self.__battery_capacity} kWh")

def main():      #funkcja uruchomienowa
    car = Car("Toyota","Camry",2023)
    electric_car = ElectricalCar("Tesla","Model 3", 2024, 75)
    car.display_info()
    car.start_production()
    car.stop_production()
    electric_car.display_info()
    electric_car.start_production()
    electric_car.stop_production()

if __name__ =="__main__":       #jeśli będzie to jako biblioteka to nie zostanie uruchomiona
    main()

