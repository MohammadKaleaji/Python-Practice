#Using a Function with a While Loop

def formatted_name(first_name, last_name):
     """Printing Full Name, neatly formatted"""
     name = f"{first_name} {last_name}"
     return name

while True:
     print("\nTell Me Your Name: ")
     print("(press 'q' to quit any time)")

     f_name = input("First Name: ")
     if f_name == 'q':
          break

     l_name = input("Last Name: ")
     if f_name == 'q':
          break
     full_name = formatted_name(f_name, l_name)
     print(f"\nHello, {full_name} !")

def greeting(names):
     """function to loop to greet list of names"""
     for name in names:
          msg = f"Hello {name.title()}"
          print(f"\n{msg}")

names_list =['hanaa', 'reem', 'ziad']
greeting(names_list)
