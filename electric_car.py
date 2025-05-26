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


class Battery:
    """A simple attempt to model a battery of an electric car"""
    
    def __init__(self, battery_size = 19):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The battery size of the car {self.battery_size}")   

    def get_range(self):
        if self.battery_size >= 20:
            range = 'High'
            print(f"The range of the car {range}")
        else:
            range = 'Low'  
            print(f"The range of the car {range}")

class Electric_Car(Car):
    """Inheritance from Car Class"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()   # adding new attribute to the inherited class
     
my_tesla = Electric_Car('Tesla', 'Electric', 2025)
print(my_tesla.car_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()