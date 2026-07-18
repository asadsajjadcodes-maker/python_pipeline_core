import json
import sys
from pathlib import Path
json_path = Path("asset_config.json")

print("Parsing multi layred pipeline configurations....")
print("----------------------------")
# Check if the configuration file exists
if not json_path.exists():
    print("Error: Target configuration file is missing.")
    sys.exit(1)
# Load the configuration file and update metadata
with open(json_path, mode="r", encoding="utf-8") as f:
    config_data = json.load(f)
    # Update the metadata section with new information
config_data["metadata"] = {
    "author": "Asad",
    "tags": ["castle", "gate", "epic"],
    "pipeline_details":{
        "engine_version": "5.4",
        "build_status": "veridied"
    }
}
# Save the updated configuration back to the file
with open(json_path, mode="w", encoding="utf-8")as f :
    json.dump(config_data, f, indent=4)# save the updated configuration back to the file
# checking the lod settings
lod_list = config_data.get("lod_settings", [])

if lod_list:
    print(f"Base mesh layer:{lod_list[0]}")
    print(f"Total lod layers registered: {len(lod_list)}")
# if there are no lod layers, print a message
else:
    print("No lod layers are found in configuration.")
# checking the author 
# # used {} to avoid KeyError if the keys are missing
author = config_data.get("metadata",{}).get("author","unknown artist")
print(f"Pipeline asset author: {author}")
# checking the engine version
#  used .get() three times to avoid KeyError if the keys are missing
engine_target = config_data.get("metadata", {}).get("pipeline_details", {}).get("engine_version", "unreal default")
print(f"Target unreal engine: {engine_target}")

print("------------------------------")
print("Nested configuration check completd with zero error.")



