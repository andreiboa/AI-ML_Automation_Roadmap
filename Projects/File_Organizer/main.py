

#main file for the file organizer project
from pathlib import Path
import organizer

folder_path = Path(input("Please enter the path of the folder you want to organize: "))

if not folder_path.exists():
    print("Folder not found.")
else:
    #Call organize_folder function to organize the files in the given directory
    print(f"Organizing files in {folder_path}...")
    organizer.organize_folder(folder_path)
    print(f"Files in {folder_path} have been organized successfully.")

