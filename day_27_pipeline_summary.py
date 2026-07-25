import argparse
import json 
import logging
import time
from pathlib import Path

#================================================================================================
#          Parse command line arguments (Extended with --report-file)
#================================================================================================
# initializing the main parser object with a clear program description for the --help menu
parser = argparse.ArgumentParser(
    description="🚀Professional pipeline asset batch auditing engine with summary exporter."
)
#Flag 1: Target directory to scan 
parser.add_argument(
    "--dir",
    type=str,
    default="test_batch_json_files",
    help="Target directory containing JSON files to audit."
)
#Flag 2: Path wher text log messages will be saved 
parser.add_argument(
    "--file-path",
    type=str,
    default="pipeline.log",
    help="Path to the output text log file on disk."
)
# Flag 3: Path where the final structured JSON metrics report will be saved 
parser.add_argument(
    "--report-file",
    type=str,
    default="audit_summary.json",
    help="Path where the final JSON audit report will be exported."
)
# Flag 4: Simulation mood for safity 
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Simulate execution without modifying the disk or loading heavy files data."
)

#Parse terminal arguments into a structured 'args' namespace object.
args = parser.parse_args()

#===============================================================================================


#===============================================================================================
#  Dual handler logging configuration 
# purpose: Dirext all system log messages to both physical file and the console output.
#===============================================================================================

# convert string path (for saving log messages) from CLI arguments into an path object
log_path = Path(args.file_path)
#configure global logging rules
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s", # log line layout
    datefmt="%Y-%m-%d %H:%M:%S", # readable time format
    handlers=[
        logging.FileHandler(log_path, mode="a", encoding="utf-8"),# append logs to disk file 
        logging.StreamHandler()# display logs directly to terminal.
    ] 
)

#===========================================================================================


#===========================================================================================
# Step 3: Resilient asset loader and verification 
# Purpose: Inspect individual JSON assets safely. Returns explicit status strings
# ("passed", "failed", "skipped") to make metric tracking straightforward in caller loops
#===========================================================================================

def process_asset(file_path, dry_run=False):
    target_path = Path(file_path)
    # dry run branch 
    if dry_run:
        logging.info(f"[Dry run] Would scan : {target_path.name}")
        return "skipped"
    # live execution branch
    logging.info(f"Scanning asset : '{target_path.name}'")
    try:
        with open (target_path, mode="r", encoding="utf-8") as f:
            data =json.load(f)
            logging.info(f"✅Asset verified : {target_path.name}")
            return "passed"
    except (FileNotFoundError, json.JSONDecodeError) as err:
        logging.error(f"❌Corrupted or invalid asset,'{target_path.name}':{err}")
        return "failed"
    except Exception as unexpected_error:
        logging.critical(f"🔥Critical failure reading '{target_path.name}': {unexpected_error}")
        return "failed"
#================================================================================================

#================================================================================================
# STEP 4: BATCH EXECUTION, METRICS ACCUMULATION & PERFORMANCE TIMING
# Purpose: Loop through directory assets, aggregate success/failure metrics, measure
# execution speed, and output terminal banners.
#================================================================================================
# capture high-precision start timestamp 
start_time = time.time()

# Target working directory initailized from CLI argument 
target_folder = Path(args.dir)

# initialize structured metrics accumulator directory
metrics ={
    "target_directory": str(target_folder),
    "total_scanned": 0,
    "passed": 0,
    "failed": 0,
    "skipped": 0,
    "execution_time_seconds": 0.0,
    "dry_run": args.dry_run
}
logging.info("="*75)
logging.info(f"CLI Pipeline Day 27 Active | Target Directory :{target_folder}")
if args.dry_run:
    logging.info("⚠️Dry run mode enabled: No file modification will occur.")
logging.info("=" * 75)

# checking if the directory exist or not
if not target_folder.exists():
    logging.error(f"❌Specified directory :{target_folder} does not exist.")
else:
    file_list = list(target_folder.rglob("*.json"))

    # store file count 
    metrics["total_scanned"]=len(file_list)
    logging.info(f"Found {len(file_list)} JSON asset in target directory {target_folder}")

    # process each asset 
    for file in file_list:
        status = process_asset(file, dry_run=args.dry_run)
        metrics[status] += 1 # dynamically increments 'passed' 'failed' 'skipped' 

    # calculate total time 
    end_time = round(time.time() - start_time, 4)
    metrics["execution_time_seconds"]= end_time

    # print Clean terminal summary 
    logging.info("=" * 75)
    logging.info("🏁CLI Batch Audit Completed.")
    logging.info(
         f"📊 Summary: {metrics['passed']} Passed | "
        f"{metrics['failed']} Failed | "
        f"{metrics['skipped']} Skipped | "
        f"Total: {metrics['total_scanned']}"
    )
    logging.info(f"Elapsed time {end_time} seconds")
    logging.info("="* 75)

    #===========================================================================================
    #  # STEP 5: AUTOMATED JSON REPORT EXPORTER
    # Purpose: Serialize runtime metrics dictionary into a readable JSON report file on disk.
    #===========================================================================================
    report_path = Path(args.report_file)

    # only write report when live execution runs 
    if not args.dry_run:
        try:
            with open(report_path, mode="w", encoding="utf-8") as f:
                json.dump(metrics, f, indent=4)
            logging.info(f"Summary sucessfully exported to '{report_path.name}'")
        except Exception as report_err:
            logging.info(f"Failed to write summary report : {report_err}")

