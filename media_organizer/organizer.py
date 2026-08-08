from pathlib import Path
from logger import log_info, log_warning, log_error


EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".json", ".html", ".css", ".js", ".cpp"],
    "others": []  # for all other files that or not in above file types 
}

def organize_folder(folder_path : str) -> dict:
    dir_path = Path(folder_path).resolve()
    if not dir_path.exists():
        log_warning(f"Target directory does not exist: '{dir_path}'")
        return {"error": f"Target directory does not exist: '{dir_path}'"}
    if not dir_path.is_dir():
        log_warning(f"Target path is not a directory: {dir_path}")
        return {"error": f"{dir_path}, is not a directory."}
    # track operational stats 
    stats = {
        "moved": 0,
        "skipped": 0,
        "categories": {}
    }
    try:
        files_list = list(dir_path.rglob("*"))
        if not files_list:
            log_info(f"No files found to organize in ,{dir_path}")
            return {"info": "No files found in folder."}
        for file in files_list:
            if file.is_file():
                
                file_ext = file.suffix.lower()
                target_category = "others" # default fallback if no match is found

                # check matching category 
                # this will iterate through the EXTENSION_MAP dictionary, where category is the key
                #  (like "Images", "Videos", etc.) and extensions is the list of file extensions associated with that category.
                for category, extensions in EXTENSION_MAP.items():
                    if file_ext in extensions:
                        target_category = category # if a match is found, set the target category to the matched category
                        break
                # create destination folder inside target directory 
                category_dir = dir_path/target_category 
                category_dir.mkdir(exist_ok= True)

                target_path = category_dir/file.name

                # prevent overwritting existing files 
                if target_path.exists():
                    log_warning(f"Skipped moving file '{file.name}' - File already exist in {target_category}")
                    stats["skipped"] += 1
                    continue
                # Safely move files 
                file.rename(target_path)
                log_info(f"Moved '{file.name}' -> '{category_dir}'")
                stats["moved"] += 1
                stats["categories"][target_category] = stats["categories"].get(target_category, 0) + 1 # it will create a new key for the category if it doesn't exist and increment the count of files moved to that category.

        return stats 

    except Exception as err:
        log_error(f"Failed during auto organization : {err}")
        return {"error": f"Organization failed: {err}"}
    
