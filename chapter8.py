def greet_user():
    """Saying Hello"""
    print("Hello Python Functions!")
    
greet_user()

def greet_user1(username):
    """Say Hello to a user"""
    print(f"Hello {username.title()}")

greet_user1('Hanaa')

def car(name, color = 'black'): # black here is default value for color
    """Display information about a car"""
    print(f"My {name.title()} is {color}")

car('Elantra', 'White')
car('Honda ciry')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

my_name = get_formatted_name('hanaa', 'benni')
print(my_name)

# Function Returns Full name, leaving the middle name optional

def get_full_name(first_name, last_name, middle_name = ''): 
    """Printing Full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
       full_name = f"{first_name} {last_name}" 
    return full_name

my_full_name = get_full_name('mohammad', 'kaleaji', 'ziad')
print(f"\n{my_full_name}")    

my_full_name1 = get_full_name('mohammad', 'kaleaji')
print(f"\n{my_full_name1}")  

def car_dic(name, model):
    """Function returns a car's name and model as a dictionary"""
    car = {'car_name': name, 'car_mode': model}
    return car

my_car = car_dic('Honda', '2024')
print(f'\n{my_car}\n')

def house(size: int, location): # indicationg size to be
    """Function returns a houes's size and location as a dictionary"""
    house_info = {'house_size': size, 'house_location': location}
    return house_info

print(house(300, 'Riyadh'))