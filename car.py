class Car:
    """A simple attempt to represent a Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        
    def car_descriptive(self):
        """neattly fromatted info about a car"""
        car = f"Car's Info: {self.make} | {self.model} | {self.year} "
        return car
    
    def read_odometer(self):
        print(f"The odometer reads at {self.odometer} miles")
        
    def update_odometer(self, milege):
        self.odometer = milege
    
my_car = Car('Lexus', 'EX', 2020)
print(my_car.car_descriptive())

my_car.odometer = 20
my_car.read_odometer()

my_car.update_odometer(30)
my_car.read_odometer()
