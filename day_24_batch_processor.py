import json
from pathlib import Path

#==========================================================================
#                     CORE UTTLITIES
#==========================================================================
# safe load json function
def safe_load_json(file_path, default_fallback=None):
    
    target_path = Path(file_path)

    try:
        with open (target_path, mode="r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as error:
        print(f"❌Error: Read warning [{file_path}]:{error}")
        return default_fallback
#--------------------------------------------------------------------
# safe save json function
def safe_save_json(data, file_path, indent=4):
    target_path = Path(file_path)
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open (target_path, mode="w",encoding="utf-8") as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as error:
        print(f"❌Error:  [{file_path}]: {error}")
        return False
    #--------------------------------------------------------------------
#========================================================================
#           BATCH PROCESSING ENGINE
#========================================================================
def process_asset_batch(input_directory, output_directory):
    # Scans input directory for all json files , applies pipeline metadata,
    # and safely exports the processed configs to output directory.
    input_path = Path(input_directory)
    output_path = Path(output_directory)
    # find all json files in the directory.
    json_files = list(input_path.rglob("*.json"))

    if not json_files:
        print(f"⚠️ No json files files found in '{input_directory}'.")

    print(f"🔍Discovered {len(json_files)} asset configuration file(s).......")
    print("------------------------------------------------------") 

    success_count = 0
    fail_count = 0

    # loop through every discovered file.
    for file in json_files:
        # loading the data safely
        data = safe_load_json(file)

        # skipping corrupted/empty json fils
        if data is None:
            print(f"Skipping corrupted/empty file: {file.name}")
            fail_count += 1
            continue # skip the rest of the code and goes to nest file in loop 

        # appling automated pipeline updates 
        data["pipeline_varified"] = True
        data["engine_target"] = "Unreal_5.4"
        # determine destination path in the output folder 
        destination = output_path/file.name

        # save processed data 
        if safe_save_json(data, destination):
            print(f"⚡Processed and saved : {file.name}-->{destination}")
            success_count += 1
        else:
            fail_count += 1

        print("--------------------------------------------------------")
        print(f"📊Batch summery :{success_count} succeeded | {fail_count} failed.")
#=========================================================================================
#                MAIN SCRIPT EXECUTTION
#=========================================================================================

print("Launching the batch asset processing core........")
print("-------------------------------------------------")

# batch process all json files 
process_asset_batch("", "batch_output")