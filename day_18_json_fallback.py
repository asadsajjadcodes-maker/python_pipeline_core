import json
import sys
from pathlib import Path
json_path = Path("asset_config.json")
print("Executing automated asset configuration parser.....")
print("-----------------------------------")
# Check if the asset_config.json file exists
if not json_path.exists():
    print("Error: Required asset_config is missing!.")
    sys.exit(1)# exit the program with an error code
# Read the JSON file and parse its contents
with open (json_path, mode="r", encoding="utf-8") as f :
    config_data = json.load(f) # parse the JSON data into a Python dictionary
# Extract the asset name from the parsed data
asset_name = config_data["asset_name"]
print(f"Asset name: {asset_name}")
# Extract the LOD count from the parsed data, with a default value of 1 if not present
lod_count = config_data.get("lod_count", 1)
print(f"Lod count (Prased or Default): {lod_count}")

# Extract the pipeline status from the parsed data, with a default value of "unknown" if not present
pipeline_status = config_data.get("pipeline_status")
print(f"Pipeline status: {pipeline_status}")
# Extract the vertex count from the parsed data, with a default value of 100 if not present
vertex_check = config_data.get("vertex_count", 100)
print(f"Vertex count: {vertex_check}")