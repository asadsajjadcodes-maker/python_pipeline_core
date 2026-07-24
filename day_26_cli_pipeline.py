import argparse
import json 
import logging 
from pathlib import Path

#====================================================================================
#  Step 1: Parse command line arguments
#====================================================================================
parser = argparse.ArgumentParser(
    description="🚀Professional Pipeline Asset Batch Auditing Engine"
)
# Defining command-line flags/arguments
parser.add_argument(
    "--dir",
    type=str,
    default="test_batch_json_files",
    help= "Target directory containing asset JSON files to audit."
)
parser.add_argument(
    "--log-file",
    type=str,
    default="pipeline.log",
    help="Path to the output log file on the disk."
)
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Simulate execution without modifying or loading heavy files."
)

args = parser.parse_args()
#=========================================================================================


#===========================================================================================
# Step 2: Configure logging from cli 
#===========================================================================================
log_path = Path(args.log_file)

logging.basicConfig(
    level= logging.INFO,# set the logging level to INFO
    format="%(asctime)s [%(levelname)s] %(message)s",# set the logging format
    datefmt="%Y-%m-%d %H:%M:%S",# set the date format
    handlers=[
        logging.FileHandler(log_path, mode="a", encoding="utf-8"),# create a file handler to write logs to the log file
        logging.StreamHandler()# create a stream handler to write logs to the console
    ]
)

logging.info("===============================================================================")
logging.info(f"CLI Pipeline Active | Target Directory: {args.dir}")
if args.dry_run:
    logging.info("⚠️Dry run mode enabled: No disk modification will occur.")

logging.info("===============================================================================")

#===============================================================================================


#===============================================================================================
#Asset loader logic
#===============================================================================================
def process_asset(file_path, dry_run=False):
    target_path = Path(file_path)

    if dry_run:
        logging.info(f"🔍[Dry run] Would scan : '{target_path.name}'")
        return True
    logging.info(f"Scanning asset: '{target_path.name}'")
    try:
        with open(target_path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"✅Asset verified : '{target_path.name}'")
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
        logging.critical(f"🔥Critical failure reading '{file_path}': '{unexpected_error}'.")
        return None
    #==========================================================================================

#==========================================================================================
# Batch execution 
#==========================================================================================
target_directory = Path(args.dir)

if not target_directory.exists():
     logging.info(f"❌Specified directory '{target_directory}' does not exist.")
else:
     file_list = list(target_directory.rglob("*.json"))
     logging.info(f"Found {len(file_list)} JSON assets in '{target_directory}'")

     for file in file_list:
          process_asset(file, dry_run=args.dry_run)

     logging.info("=======================================================================")
     logging.info("🏁 CLI Batch Audit Completed")
     logging.info("=======================================================================")
     