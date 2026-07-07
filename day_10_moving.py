from pathlib import Path
# current working directory
current_dir = Path("")
# Creating a directory structure for the example 
source_file = current_dir/ "raw_texture.txt"
# Creating a temporary file to simulate a raw texture asset
source_file.write_text("This is raw texture data.")
print(f"Generated a temporary asset: {source_file.name}")
# Creating the destination directory structure
destination = current_dir/"Unreal_Exports"/"Textures"/"Archive"/"moved_texture.txt"
print(f"Moving asset to destination:{destination}")
print("------------------------------------")
# checking if the destination directory exists
target_dir = current_dir/"Unreal_Exports"/"Textures"/"Archive"
result= target_dir.exists()
if result == False:
    print("Creating the destination directory structure since it does not exist.")
    print("------------------------------------")
    target_dir.mkdir(parents=True, exist_ok=True)
    

# Moving the file to the destination
source_file.rename(destination)
# Checking if the original file still exists and if the file arrived at the destination
print("Does the original file still exist here:",source_file.exists())
# Checking if the file arrived at the destination
print("Did the file arrive the at the destination:",destination.exists())