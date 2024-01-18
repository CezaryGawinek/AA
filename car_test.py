#pip install pytest
import pytest
from car import Car, ElectricalCar

@pytest.fixture
def get_car():
    return Car("Toyota", "Camry", 2023)

@pytest.fixture
def get_electricalcar():
    return Car("Tesla","Model 3",2024,75)

def test_car_display_info(get_car):
    expected_output = "Marka: Toyota\nModel: Camry\nRocznik: 2023\nCzy jest aktualnie produkcja? Nie"
    assert get_car.display_info() == expected_output

def test_car_start_production(get_car):
    get_car.start_production()
    assert get_car.__is_production() is True
    get_car.stop_production()
    assert get_car.__is_production is False