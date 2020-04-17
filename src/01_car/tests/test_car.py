from dataclasses import asdict

from car import create_car_from_name, Transmission, TR_MANUAL


def test_create_car_from_name(data_regression):
    car = create_car_from_name("Toyota Corolla 1999")
    assert car.manufacturer == "Toyota"
    assert car.model == "Corolla"
    assert car.transmission == Transmission(n_speed=5, type_=TR_MANUAL)
    assert car.year == 1999
    assert car.power == 120
    assert car.torque == 165


def test_create_car_from_name_regression(data_regression):
    car = create_car_from_name("Mazda MX-5 2015")
    data_regression.check(asdict(car))
