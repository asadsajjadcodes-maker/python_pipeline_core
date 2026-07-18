import json
import sys
from pathlib import Path

# Definig the machine (the function)
""" 
    Takes an asset configuration dictionary, safely extracts key values and returns a clean
    user-friendly summary string.
    """

def get_asset_summary(asset_dictionary):
    # Safely extract values from the asset dictionary with default fallbacks with the .get() method
    name = asset_dictionary.get("asset_name", "unknown_asset")
    vertices = asset_dictionary.get("vertex_count", 0)
    author = asset_dictionary.get("metadata", {}).get("author", "unknown_artist")
    
    summary_string = f"Asset: {name}, Created by author: {author}, Has a density of {vertices} vertices"
    return summary_string # return the summary string

json_path = Path("asset_config.json")
# Check if the JSON file exists before attempting to read it
if not json_path.exists():
    print("Error: Target configuration file is missing.")
    sys.exit(1)
# Read the JSON file and load its contents into a dictionary
with open(json_path, mode="r", encoding="utf-8") as f:
    config_data = json.load(f)
# Use the get_asset_summary function to process the configuration data and print the result
config_data = get_asset_summary(config_data)
print(config_data)
# Process fake data to demonstrate the function's behavior with missing keys
fake_data_dict = {}
fake_data_summary = get_asset_summary(fake_data_dict)
print(fake_data_summary)
