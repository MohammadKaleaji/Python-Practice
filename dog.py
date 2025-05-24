class Dog:
     """A simple Atempt to Mpdel a Dog"""
     def __init__(self, name, age):
          """Initialize name and age attributes"""
          self.name = name
          self.age = age

     def sit(self):
          """Simulates Dog's sitting in respond to commands"""
          print(f"{self.name} is now sitting")

     def roll_over(self):
          """Simulates Dog's roll-over in respond to commands"""
          print(f"{self.name} is now rolling over")

#Making an instance from class

my_dog = Dog('Willy', 5)

print(f"My dog's name is: {my_dog.name}\n") # Testing if instance getting the attribute name from Dog class
print(f"My dog's age is: {my_dog.age}\n") # Testing if instance getting the attribute age from Dog class

my_dog.sit() # Testing the Dog classs sit Method
my_dog.roll_over() # Testing the Dog classs roll-over Method

dog2 = Dog('dogy', 6)
print(f"My dog's name is: {dog2.name}\n") 
print(f"My dog's age is: {dog2.age}\n")
dog2.sit()
dog2.roll_over()
