
#For practicing pathlib libray in python
from pathlib import Path

path = Path(r"C:\Users\Boa\Documents\GitHub\AI-ML-Automation_Roadmap")

print(f"Exists: {path.exists()} \n"
      f"Directory: {path.is_dir()}")

for file in path.iterdir():
    print(file.name)

for file in path.iterdir():
    if file.is_file():
        print(f"File: {file.name} \n"
              f"Extension: {file.suffix} \n")
        
    
