import sys
import json
from pathlib import Path 
json_path = Path("asset_config.json")
print("Opening the stream to read and parse the asset structure data....")
print("-------------------------------------")

if json_path.exists(): # this will check if the file exists or not
    # open the file in read mode and parse the data
    with open (json_path, mode="r", encoding="utf-8") as f:
        # read the data from the file and parse it into a dictionary
        config_data = json.load(f)
else:
    print("The file do not exist....")
    sys.exit(1) # exit the program with an error code
# assign the values to variables using the keys of the dictionary
asset_name = config_data["asset_name"]
has_collision = config_data["has_collision"]
export_directory = config_data["export_directory"]
print(f"Parsed asset name: {asset_name}")
print(f"Does it has collision: {has_collision}")
print(f"Target export folder: {export_directory}")
print("---------------------")
print("Checking the type of the has_collision.....")
print(type(has_collision)) # checking the type of the has_collision variable
print("Data was read successfully.")
print("------------------------------")
print("Displaying the full data of file .....")
print("---------------------------")
print(config_data)

