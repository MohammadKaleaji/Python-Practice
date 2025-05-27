from pathlib import Path

print("Current working directory:", Path.cwd())  # Debug: See where Python is looking
path = Path("Python-OOP.txt")
content = path.read_text()
print(content)