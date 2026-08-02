

#For practicing shutil library in python
from pathlib import Path
import shutil


print("Moving file...")
source = Path(r"C:\Users\Boa\Documents\GitHub\AI-ML-Automation_Roadmap\Exercises\Libraries\shutil\test_file.txt")
destination = Path(r"C:\Users\Boa\Documents\GitHub\AI-ML-Automation_Roadmap\Exercises\Libraries\shutil\TestFolder")

destination.mkdir(exist_ok=True)

shutil.move(source, destination)
print("Done!")