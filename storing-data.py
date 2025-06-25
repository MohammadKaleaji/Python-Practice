from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11]

path = Path("numbers.json")      # get the path
contents = json.dumps(numbers)   # store the numbers in the json file
path.write_text(contents)        #write the conents in the path ==> json file 