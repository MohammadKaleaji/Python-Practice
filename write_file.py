from pathlib import Path

path = Path("/home/kaleaji/Desktop/python-clone/Python-Practice/file1.txt")

content = "I love programming\n"
content+= "I love Testing|QA\n"
content+= "I love Python\n"

path.write_text(content)

