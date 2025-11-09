from classes.car import Car
from classes.electric_car import ElectricCar
from classes.engine import Engine
from classes.track import Track

if __name__ == "__main__":
    track = Track(23665765, 2019, 200000)
    car = Car(67329874, 2009, Engine(1500, "Toyota"))
    electric_car = ElectricCar(67342310, 2015, Engine(2000, "Tesla"))
    cars_lst = [track, car, electric_car]
    for i in cars_lst:
        print(i.calculate_annual_tax())

    car.set_year(2008)
    print(car.get_year())

    electric_car.charge()
    print(electric_car.get_luxury_feature())