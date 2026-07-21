import json
from pathlib import Path

# reuseable uttlity function (safe saver)
#===========================================

def safe_save_json(data, file_path, indent=4):
    """
    Safely writes the data (dict/list) to a json file.
    Creates missing sub directories automatically, handles write errors,
    and returens True on success and False on failure.
    """
    target_path = Path(file_path)
    try:
        # step 1 : Ensure parent folders exist! 
        # Create automatically sub-folders if missing 
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Step 2: write the json data cleanly 
        with open(target_path, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent)

        print(f"✅ Success: file saved cleanly to {target_path}")
        return True

    except PermissionError:
        print(f"❌ Error: Permission denied with writing to {file_path}. File maybe locked.")    
        return False
    except TypeError as error:
        print(f"❌ Error: Data contains non- JSON serializable objects! {error}")
        return False
    except Exception as unexpected_error:
        print(f"❌ Error: Unexpected write error on {file_path} : {unexpected_error} ")
        return False
    #=================================================================

# reuseable uttlity function (safe loder)  
#=============================================

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

#================================================================


print("Launching safe_saver test suite....")
print("-----------------------------")

sample_data = {
    "asset_name": "SM_Castle_Gate_V02",
    "status": "ready_for_engine",
    "export_count": 1
}

# Writing to new nested directory that dose not exist yet.
output_file = "build_output/configs/procssed_asset.json"
# calling the function

success = safe_save_json(sample_data, output_file)

if success: 
    print(f"Pipeline status : output generated successfully at {output_file}.")

else:
    print("Pipeline status : Failed to save the output config.")


print("loading the saved data......")
print("-------------------------")
config_data = safe_load_json(output_file)

#=========================

print("----------------------")
print("All tests executed cleanly.")
