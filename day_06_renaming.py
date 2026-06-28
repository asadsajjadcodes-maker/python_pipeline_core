from pathlib import Path 
original_path = Path("D:/UnrealProjects/Game/Content/Textures/T_Brick_Wall_D.png")
new_map_asset = original_path.with_name("T_Brick_Wall_D_01.png") # this will swap the name of the file 
print("1. New path with swapped filename:")
print(new_map_asset)
print("----------------------------")
engine_asset = original_path.with_suffix(".uasset") # this will swap the suffix of the file
print("2. New path with swapped suffix: ")
print(engine_asset)
secret_path = original_path.with_name("SM_castle_gate.fbx").with_suffix(".obj") # method chaining
print(secret_path)