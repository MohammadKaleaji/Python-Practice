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
        if milege >= self.odometer:
            self.odometer = milege
        else:
            print("You Can't Roll-Back the Odometer read! ")
    def increment_odometer(self, milege):
        self.odometer += milege

class Electric_Car(Car):
    """Inheritance from Car Class"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
     
my_tesla = Electric_Car('Tesla', 'Electric', 2025)
print(my_tesla.car_descriptive())
