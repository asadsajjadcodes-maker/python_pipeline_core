import json
from pathlib import Path
# making a utility function to safely load json files with error handling and fallback mechanism
def safe_load_json(file_path, default_fallback = None):
    if default_fallback is None:# if no fallback is provided, use an empty dictionary as the default
        default_fallback = {}
    target_path = Path(file_path) # convert the file path to a Path object for better handling of file paths
    try:# Attempt to open and read the JSON file
        with open (target_path, mode="r", encoding="utf-8") as f:
            return json.load(f) # return the loaded JSON data if successful
    # file not found error handling    
    except FileNotFoundError:
        print(f"Warning: File {file_path}, not found. Using fallback.")
        return default_fallback # return the default fallback if the file is not found
    # JSON decode error handling if file is corrupted or not a valid JSON
    except json.JSONDecodeError as error:
        print(f"Error: File {file_path},is corrupted! {error}")
        return default_fallback
    # Catching any other unexpected errors that may occur during file reading
    except Exception as unexpected_error:
        print(f"Unexpected error reading {file_path}:{unexpected_error}")
        return default_fallback
    
print("Launching the utility function..... ")
print("-------------------------")
# Test 1 
# Reading a healthy file 
# loading a valid JSON file and extracting the asset name from it
valid_config = safe_load_json("asset_config.json")
asset_name = valid_config.get("asset_name", "unknown_asset") 
print(f"Healthy file load ->Asset name:{asset_name}")
# Test 2
# Reading a completely missing file (with a custom fallback)
# if custom fallback is provided, it will be used instead of the default empty dictionary
# if custom fallback is not provided, the default empty dictionary will be used
missing_config = safe_load_json("missing_file.json", default_fallback= {"status": "missing_asset"})
print(f"Missing file load -> Result: {missing_config}")

print("------------------------------------------")
print("All loader tests executed cleanely.")
