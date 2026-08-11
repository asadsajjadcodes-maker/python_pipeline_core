from pathlib import Path
from logger import log_info, log_warning, log_error

# File categorization by extension mapping
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".json", ".html", ".css", ".js", ".cpp"],
    "others": []  # Fallback category for unmatched file extensions
}

def organize_folder(folder_path: str) -> dict:
    """
    Organizes files into subdirectories based on extension types.
    Logs each action via triple logging and returns statistical summary dictionary.
    """
    dir_path = Path(folder_path).resolve()
    
    # Validate directory availability
    if not dir_path.exists():
        msg = f"Target directory does not exist: '{dir_path}'"
        log_warning(msg)
        return {"error": msg}
        
    if not dir_path.is_dir():
        msg = f"Target path is not a directory: '{dir_path}'"
        log_warning(msg)
        return {"error": msg}

    # Initialize statistics counters
    stats = {
        "moved": 0,
        "skipped": 0,
        "categories": {}
    }

    try:
        files_list = list(dir_path.rglob("*"))
        if not files_list:
            log_info(f"No files found to organize in '{dir_path}'")
            return {"info": "No files found in folder."}

        for file in files_list:
            if file.is_file():
                file_ext = file.suffix.lower()
                target_category = "others"

                # Identify category based on extension
                for category, extensions in EXTENSION_MAP.items():
                    if file_ext in extensions:
                        target_category = category
                        break

                # Target subfolder setup
                category_dir = dir_path / target_category
                
                # Prevent moving files that are already inside a category directory
                if file.parent == category_dir:
                    continue

                category_dir.mkdir(exist_ok=True)
                target_path = category_dir / file.name

                # Skip existing destination files to avoid overwriting
                if target_path.exists():
                    log_warning(f"Skipped moving file '{file.name}' - File already exists in {target_category}")
                    stats["skipped"] += 1
                    continue

                # Safely relocate file
                file.rename(target_path)
                log_info(f"Moved '{file.name}' -> '{category_dir}'")
                stats["moved"] += 1
                stats["categories"][target_category] = stats["categories"].get(target_category, 0) + 1

        return stats

    except Exception as err:
        log_error(f"Failed during auto organization: {err}")
        return {"error": f"Organization failed: {err}"}