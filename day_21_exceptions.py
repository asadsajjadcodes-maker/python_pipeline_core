import json
import sys
from pathlib import Path
# create a path object for the json file
json_path = Path("asset_config.json")

print("Launching day 21 secure asset core ingestion......")
print("--------------------------------------")

# try to open the json file and parse it, if it fails, handle the exception gracefully
try: # try is an exception handling block that allows you to catch and handle exceptions. 
    with open (json_path, mode="r", encoding="utf-8") as f:
        config_data = json.load(f)

    print(f"Success! Parsed Asset:{config_data.get("asset_name", "unknown")}")
# handle the exception if the file is not found .
except FileNotFoundError:
    print("Backup Triggered: The configuration file was not found on the disk.")
    config_data = {}
# handle the exception if the json file is corrupted or broken
except json.JSONDecodeError as error_details :
    print("Backup Triggered: The JSON file is corrupted or broken.")
    print(f"Analysis Details: {error_details}")
    config_data = {}
#print the current runtime data state and system status
print("----------------------------------------------")
print(f"Current runtime data state: {config_data}")
print("System status: Script finished execution cleanly without crashing .")
    


