from dataclasses import asdict

from car import create_car_from_name


def test_create_car_from_name_regression(data_regression):
    car = create_car_from_name("Toyota Corolla 1999")
    data_regression.check(asdict(car))
