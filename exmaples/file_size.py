import os

file = os.stat("exmaples/kal.txt")
print(f"{file.st_size} byte")       #st_size