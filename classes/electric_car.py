from classes.car import Car
from classes.electricmixin import ElectricMixin
from classes.luxurymixin import LuxuryMixin


class ElectricCar(Car, ElectricMixin, LuxuryMixin):
    def calculate_annual_tax(self):
        return 250