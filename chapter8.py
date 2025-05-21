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