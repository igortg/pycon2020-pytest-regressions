from dataclasses import dataclass

@dataclass
class Transmission:
    n_speed: int
    type_: str

TR_AUTO = 'automatic'
TR_MANUAL = 'manual'

@dataclass
class Car:
    manufacturer: str
    model: str
    transmission: Transmission
    year: int
    displacement: float  # in cc
    power: float  # in hp
    torque: float  # in Nm


def create_car_from_name(name):
    """Search in some database and return a Car"""
    car = Car(
        manufacturer = 'Toyota',
        model = 'Corolla',
        transmission = Transmission(n_speed=5, type_=TR_MANUAL),
        year = 1999,
        displacement = 1794,
        power = 120 ,
        torque = 165,
    )
    return car
