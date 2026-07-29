from logger_config import setup_pipeline_logger
from asset_scanner import asset_scan
from pathlib import Path
import argparse


def main():
    logger = setup_pipeline_logger("day29_run.log")

    parser = argparse.ArgumentParser(
        description="Media asset auditer"
    )
    parser.add_argument(
        "--dir",
        type=str,
        default= "",
        help="Folder for scanning"
    )
    args = parser.parse_args()
    

    logger.info(f"Scanning the folder: {args.dir}")
    result = asset_scan(args.dir) # args.dir takes the directory entered in CLI
    if "error" in result:
        logger.error(result["error"])
    else:
        total_image = len(result["pictures"])
        total_videos = len(result["videos"])
        other_files = len(result["other"])
        logger.info(f"total images found {total_image}")
        logger.info(f"total videos found {total_videos}")
        logger.info(f"other files found {other_files}")
        logger.info(f"total size of assets {result['total_size_mb']} mb")

if __name__ == "__main__":
    main()

    

