from pathlib import Path
engine_content_dir = Path("D:/UnrealProjects/Game/Content") # Engine content directory
sub_folder = "Textures" # Sub-folder name
target_folder = engine_content_dir/sub_folder # joining the engine content directory with the sub-folder name
final_asset_path = target_folder/"T_Brick_Wall_D.png" # adding the asset file name to the target folder path
print("1. Combined folder path:")
# Print the combined folder path
print(target_folder)
print("---------------")
print("2. Final target asset path:")
# Print the final target asset path
print(final_asset_path)
print("--------------")
print("3. Extension of the asset file:")
print(final_asset_path.suffix)# Print the extension of the asset file
