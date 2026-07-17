import json
import sys
from pathlib import Path
json_path = Path("asset_config.json") # Path to the JSON configuration file
print("Modifying pipeline configuration data dynamically.....")
print("-------------------------------------------")
# Check if the JSON file exists
if not json_path.exists():
    print("Error: Target configuration file not found.")
    sys.exit(1)# exit the script if the file does not exist
# Read the existing JSON data
with open (json_path, mode="r", encoding="utf-8") as f:
    config_data = json.load(f)
print(f"Original vertex count: {config_data["vertex_count"]}")
print(f"Original collision flag: {config_data["has_collision"]}")
# Modify the configuration data
config_data["vertex_count"] = 9999 # Update the vertex count to a new value
config_data["has_collision"] = False # Update the collision flag to False
# Add a new key-value pair to indicate optimization completion.
# you can add any additional modifications or new keys as needed.
# because the JSON file is a dictionary, you can add new keys by simply 
# assigning a value to a new key name.
config_data["optimization_completed"] = True
# Write the modified data back to the JSON file
with open (json_path, mode="w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=4) # indent=4 for pretty printing

print("Successfully modified and updated asset_config.json on disk.")
