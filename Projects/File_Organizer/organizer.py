

#Would organize the files in the given directory based on their extensions
from pathlib import Path
import shutil
import file_types

#Get file_types.py file and check the extension of the file and return the category of the file
def get_category(path):
    if path.suffix in file_types.DOCUMENTS:
        return "Documents" 
    elif path.suffix in file_types.PHOTOS:
        return "Photos"
    elif path.suffix in file_types.VIDEOS:
        return "Videos"
    elif path.suffix in file_types.AUDIO:
        return "Audio"
    return None

def move_file(file, directory, category):
    destination = directory / category
    destination.mkdir(exist_ok=True)
    shutil.move(str(file), str(destination / file.name))

def organize_folder(directory):
    for file in directory.iterdir():
        if file.is_file():
            category = get_category(file)
            if category:
                move_file(file, directory, category)

