from pathlib import Path
build_folder = Path("Unreal_Exports/Textures/Archive") # this is the path to the folder we want to create
print("Attempting to generate the folder structure:")
print("-----------------------------")
build_folder.mkdir(parents= True, exist_ok= True) # this will create the folder structure if it does not exist, and will not throw an error if it already exists
print("Dose the new folder exist now:", build_folder.exists())# this will check if the folder exists and print the result
print("Is is actually a directory:" , build_folder.is_dir())# this will check if the path is a directory and print the result
