from pathlib import Path
from logger_config import setup_pipeline_logger


def asset_scan(folder_path: str) -> dict:
    logger = setup_pipeline_logger("day29_run.log")
    target_path = Path(folder_path).resolve()
    if not target_path.exists() or not target_path.is_dir():
        return {"error": f"❌Error, '{target_path}' does not exist or its not a directory."}

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
    summary = {
        "total_scanned": 0,
        "pictures": [],
        "videos": [],
        "other": [],
        "total_size_mb": 0 
    }

   
    
    file_list = list(target_path.rglob("*"))

    for file in file_list:
        if file.is_file:
            ext = file.suffix.lower()
            
            file_size = round(file.stat().st_size/(1024 * 1024),2)
            summary["total_scanned"] += 1
            summary["total_size_mb"] += file_size

            if ext in IMAGE_EXTENSIONS:
                logger.info(f"picture detected: {file.name}")
                summary["pictures"].append(file.name)
            if ext in VIDEO_EXTENSIONS:
                logger.info(f"video detected: {file.name}")
                summary["videos"].append(file.name)
            else:
                summary["other"].append(file.name)


    return summary
    
