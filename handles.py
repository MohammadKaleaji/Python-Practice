"""from pathlib import Path

file_path = Path("Python-OOP.txt")
content = file_path.read_text()
lines = content.splitlines()

print(lines)"""

try:
    # comment: 
    print(5 / 0)
except Exception as DivisionbyZero:
    print("You can't divide on Zerp")
# end try


num1 = int(input("Enter number: "))
num2 = int(input("Diivde it by what: "))

try:
    # Check if dividing by zero
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    result = num1 / num2
    print(f"The result of the proccess: {result}")
except ZeroDivisionError as e:
    print("You can't divide by zero!")


