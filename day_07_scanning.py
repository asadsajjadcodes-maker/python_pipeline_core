from pathlib import Path
current_repo = Path("") # it represents the current working directory
print("Scanning the python_pipeline_core folder: ") 
for item in current_repo.iterdir(): # iterate over all items in the directory
    if item.is_file(): # check if the item is a file not a folder
        print(f"Found item: {item.name}") # print each found item
        