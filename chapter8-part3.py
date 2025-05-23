printed = ['phone case', 'laptop', 'glasses']
unprinted = []

# Function to loop throw printed , pop element and append it to unprinted
def add_unprinted(printted_list, unprinted_list):
     while printted_list:
          current_item = printted_list.pop()
          print(f"The printed Item {current_item}")
          unprinted_list.append(current_item)

def show_printed(unprinted_list):
     print(f"\nThis is the list of Newly Printed Items: ")
     for item in unprinted_list:
          print(item)

add_unprinted(printed[:], unprinted) # the [:] says to python that the edits was just a copy of printed list 
show_printed(unprinted)              # and keep the original items of printed list in line 1

print(printed) #Testing [:]

# Passing arbitary argument to dunction

def pizza(*toppings):
     """Print topiings of Pizza"""
     print(toppings)
     
pizza('mashrom', 'sauce', 'peproni')

# mixing positional and aribitary arguments 

# def make_pizza(size, *toppings):
#      """print Pizza Info"""
#      for topping in toppings:
#           print(f"- {topping}") # to print (*toppings) with its unknown length 
#      print(f"You have ordered a {size} and {toppings} topings")
#     
# make_pizza('Large', 'ketchep', 'mayo', 'bbq')

def make_pizza(size, *toppings):
    """Print Pizza Info (size can be str or int)"""
    for topping in toppings:
        print(f"- {topping}")
    print(f"You have ordered a {size}-inch pizza with toppings: {toppings}")

make_pizza('Large', 'ketchup', 'mayo', 'bbq')  # Now size accepts strings

def build_profile(first, last, **info):
     info['first_name'] = first
     info['last_name'] = last
     return info

user1 = build_profile('Mohammad', 'Kaleaji', location = 'istanbul', career = 'SQA')
print(user1)
