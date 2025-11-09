from classes.engine import Engine
from classes.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, license_plate, year, engine: Engine):
        super().__init__(license_plate, year)
        self.engine = engine

    def calculate_annual_tax(self):
        if self.get_year() > 2010:
            return self.engine.horsepower * 0.17 + 200
        return self.engine.horsepower
    