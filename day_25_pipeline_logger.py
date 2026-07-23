import json
import logging
from pathlib import Path

#==============================================================================================
#                        Initialize dual-channel logging
#==============================================================================================
# create a path object for the log file
log_file = Path("pipeline.log")
# it will create the log file if it doesn't exist, and append to it if it does
logging.basicConfig(
    level= logging.INFO,# set the logging level to INFO
    format="%(asctime)s [%(levelname)s] %(message)s",# set the logging format
    datefmt="%Y-%m-%d %H:%M:%S",# set the date format
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),# create a file handler to write logs to the log file
        logging.StreamHandler()# create a stream handler to write logs to the console
    ]
)
#==============================================================================================
# logging.info works like print, but it writes to the log file and console
logging.info("================================================================")
logging.info("🚀Pipeline Engine Started(Day 25 logging core)")
logging.info("===========================================================")

#=============================================================================================
#      Logged asset loader
#============================================================================================

def load_and_varify_asset(file_path):
    target_path = Path(file_path)
    logging.info(f"Scanning the file '{target_path.name}'")
    try:
        with open (target_path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"✅Asset varified: '{target_path.name}' loaded cleanly.")
            return data
    except FileNotFoundError:
        #.warning is used for non-critical issues that should be noted,
        #  but do not stop the program from running 
        logging.warning(f"⚠️Missing file: '{file_path}' was not found on disk.")
        return None
    except json.JSONDecodeError as decode_error:
        # .error is used for serious issues that may prevent the program from running correctly
        logging.error(f"❌Corrupted asset:'{file_path}' contains invalid json syntax ({decode_error}) ")
        return None
    except Exception as unexpected_error:
        # .critical is used for very serious issues that will likely cause the program to stop running
        logging.critical(f"🔥Critical faliure reading '{file_path}': '{unexpected_error}'.")
        return None

#=================================================================================================
#          test execution suit
#===============================================================================================

target_file = Path("test_batch_json_files")
file_names = ["missing_file.json"]# a missing file to test the logging of a missing file
counter = 0
for file in target_file.rglob("*"):# rglob is used to recursively search for all files in the target directory and its subdirectories
    file_names.append(file)# append each found file to the list
    counter += 1
# varify each asset in the list of file names
for asset in file_names:
    load_and_varify_asset(asset)
logging.info("-------------------------------------------")
logging.info(f"🏁Batch verification run completed, {counter} files scanned.")
logging.info("--------------------------------------------------")
#=======================================================================================