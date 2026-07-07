from pathlib import Path
build_folder = Path("Unreal_Exports/Textures/Archive")
print("Attempting to generate the folder structure:")
print("-----------------------------")
build_folder.mkdir(parents= True, exist_ok= True)
print("Dose the new folder exist now:", build_folder.exists())
print("Is is actually a directory:" , build_folder.is_dir())
