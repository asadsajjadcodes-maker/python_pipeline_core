from pathlib import Path
asset_path = Path("D:/UnrealProjects/MedievalGame/Content/Characters/Knight/SM_Knight.fbx") # Path to the asset file
print("1. Direct parent folder:")
print(asset_path.parent)# This will give you the parent folder of the asset, which is "D:/UnrealProjects/MedievalGame/Content/Characters/Knight" in this case.
print("--------------------")
print("2. The grandparent folder:")
print(asset_path.parent.parent) # This will give you the grandparent folder of the asset, which is "D:/UnrealProjects/MedievalGame/Content/Characters" in this case.
print("--------------------")
print("3. Only name of the parent folder:")
print(asset_path.parent.name) # This will give you just the name of the parent folder, which is "Knight" in this case.
print("---------------------")
print("4. Only name of the grandparent folder:")
print(asset_path.parent.parent.name) # This will give you just the name of the grandparent folder, which is "Characters" in this case.


