from random import randint, choice
#from random import choice

num = randint(2, 99)
print(num)

names = ['mohammad', 'reem', 'ziad', 'hanaa']
name = choice(names)
print(f"Selected Player {name.title()}")