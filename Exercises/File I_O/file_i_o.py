

#For learning File I/O in python
from pathlib import Path



file_input = input("Please enter the path of the file you want to read: ")
file_path = Path(file_input)

#For checking which directory the file is in
print(Path.cwd())

with file_path.open("r") as file:
    content = file.read()

print(f"File Contents: \n{content}")

with file_path.open("a") as file:
    file.write("\n50")

with file_path.open("r") as file:
    updated_content = file.read()

print(f"Updated contents: \n{updated_content}")