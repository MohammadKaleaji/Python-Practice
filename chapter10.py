from pathlib import Path

def count_words(path):
     try:
          contents = path.read_text(encoding = 'utf-8')
     except FileNotFoundError:
          print(f"Sorry the file you are looking for {path} not found")
     else:
          # count approximate number of words in the file
          words = contents.split()
          num_words = len(words)
          print(f"The file {path} has {num_words} words")




path = Path('example.txt') # defifing the path
count_words(path) # calling the function and pass the file stored variable "path"
