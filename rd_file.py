from pathlib import Path

path = Path("/home/kaleaji/Desktop/python-clone/Python-Practice/pi_num1.txt") 
path.write_text("I love programming!") # looking if file in the path exisit delete all content on it and write this line
content = path.read_text()             # if no file exisit, it creats one with name on the path and write on it
lines = content.splitlines()

pi_string = ''
for line in lines:
     pi_string+=line

print(pi_string)
print(len(pi_string))

birthday = input("Enter your birthday in this format 'mmddyy': " )

if birthday in pi_string:
     print(f"your birthday {birthday} are in the pi digits")
else:
     print(f"Sorry your birthday {birthday} are not in the pi digits")   