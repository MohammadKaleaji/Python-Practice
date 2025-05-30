from pathlib import Path

file_path = Path("Python-OOP.txt")
content = file_path.read_text()
lines = content.splitlines()

print(lines)
