from pathlib import Path
import json # importing json module to work with json files
target_path = Path("asset_config.json")# creating a path object for the json file
# creating a dictionary to hold asset metadata
asset_metadata = {
    "asset_name": "SM_Castle_Gate_V02",
    "vertex_count": 14205,
    "has_collision": True,
    "lod_settings": ["LOD_0", "LOD_1","LOD_2"],
    "export_directory": "Unreal_Exports/Textures"

}

print("Serializing dictionary data into asset_config.json....")
print("----------------------------------")
# writing the dictionary data into a json file
with open (target_path, mode="w", encoding="utf-8") as f:
    # dumping the dictionary data into the json file with indentation for better readability
    json.dump(asset_metadata, f, indent=4) 
print("Json file generated successfully.")
