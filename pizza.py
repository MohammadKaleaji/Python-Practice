def make_pizza(size, *toppings):
    """Print the info of Pizza"""
    print(f"You Have Ordered {size} with these: ")
    for topping in toppings:
        print(f"-{topping}")
        

    