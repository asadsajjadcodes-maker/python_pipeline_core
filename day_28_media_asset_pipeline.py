from pathlib import Path
import os
import sys
import argparse
import logging # logging module 

#========================================================================================
# Pipeline logging configuration 
# log for both terminal and for log file on disk
#========================================================================================
log_file_path = Path.cwd()/"media_pipeline.log"
print(log_file_path)
logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_file_path, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
#========================================================================================

#========================================================================================
# Asset Category constants
# Define allowed formats for classification in the pipeline
#========================================================================================
# image extensions
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", 
    ".tiff", ".tif", ".webp", ".svg", ".heic", 
    ".heif", ".raw", ".cr2", ".nef", ".ico"
}
# video extensions
VIDEO_EXTENSIONS = {
    ".mp4", ".mkv", ".avi", ".mov", ".wmv",
    ".flv", ".webm", ".m4v", ".mpeg", ".mpg",
    ".3gp", ".3g2", ".ogg", ".ogv", ".vob"
}

#==========================================================================

# function for checking the media type in target folder and sub-folders in it.

def audit_media(target_dir: str) -> dict:
    dir_path = Path(target_dir) # converts the string to a Path object 

    # checking if the target directory exists or it is a directory not a file 
    if not dir_path.exists():
        logging.error(f"❌Failed: Target path '{dir_path}' does not exist.")
        sys.exit()
    elif not dir_path.is_dir():
        logging.error(f"❌Failed: Target path '{dir_path}' is not a directory.")
        sys.exit()

    # Structure to hold categorized asset paths and sizes
    summary = {
        "pictures":[],
        "videos":[],
        "others":[],
        "total_size_bytes":0,
        "total_files_audited":0
    }
    logging.info(f"Starting asset audit in directory: '{dir_path.resolve()}'.........")
    logging.info(".............................................")
    #scanning the directory recursively
    
    for file in dir_path.rglob("*"):
        if file.is_file():
            extension = file.suffix.lower() # converts the extension in lower case
            file_size = file.stat().st_size # check the size of the file
            summary["total_size_bytes"] += file_size
            summary["total_files_audited"] += 1

            # asset metadata record
            asset_info = {
                "name": file.name,
                "path": str(file.resolve()),
                "size_mb": round(file.stat().st_size/ (1024 *1024),2) # convert bytes to MB. the ,2 is for rounding to 2 decimal places   
            }

            # Classify based on the file extension
            if extension in IMAGE_EXTENSIONS:
                summary["pictures"].append(asset_info)
                logging.info(f"[Picture Detected]:'{file.name}' ({asset_info['size_mb']}MB)")
            elif extension in VIDEO_EXTENSIONS:
                summary["videos"].append(asset_info)
                logging.info(f"[Video Detected]:'{file.name}' ({asset_info['size_mb']}MB)")
            else:
                summary["others"].append(asset_info)

    return summary
#============================================================================================
def main():
    #Setup CLI argument parser
    parser = argparse.ArgumentParser(
        description="Pipeline core: Audit ans categorize pictures and video asset in a folder."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="",
        help="Path to directory containing media asset (default= current directory)."
    )
    args = parser.parse_args()

    # executing the asset procss logic
    result = audit_media(args.dir)

    # out put summery if audit completed
    print(".............................")
    print(f"Total Files Audited: {result['total_files_audited']}")
    print(f"Pictures Found: {len(result['pictures'])}")
    print(f"Videos Found: {len(result['videos'])}")
    print(f"Other Files: {len(result['others'])}")
    print(f"Total_size: ({round(result['total_size_bytes']/(1024 *1024),2)} MB)")
    print("------------------------------")
    print(f"Audit for directory '{args.dir}' has successfully completed.")
#=======================================================================================

if __name__=="__main__":
    main()
