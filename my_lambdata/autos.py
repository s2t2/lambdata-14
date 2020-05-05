# autos.py

class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        """
        Params:
            make str ...
            model str ...
            year int ...
            color str ...
            num_wheels int  ...
        """

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("WE ARE DRIVING", self.model)

    def advertise(self):
        print("BUY OUR", self.model)

class Truck(Auto):
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels)
        self.bed_size = bed_size

if __name__ == "__main__":

    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    print(car.make)
    print(car.model)
    car.drive()
    car.advertise()

    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    print(car2.make)
    print(car2.year)
    car2.drive()
    car2.advertise()

    truck = Truck("Tesla", "Cybertruck", 2020, "Silver", 8, "4x6")
    print(truck.make)
    print(truck.model)
    print(truck.year)
    print(truck.bed_size)
    truck.drive()
    truck.advertise()
