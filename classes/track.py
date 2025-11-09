from classes.vehicle import Vehicle


class Track(Vehicle):
    def __init__(self, license_plate, year, max_load):
        super().__init__(license_plate, year)
        self.max_load = max_load

    def calculate_annual_tax(self):
        if self.max_load > 300000:
            return self.get_year() * 0.17 + 500
        return self.get_year() * 0.17