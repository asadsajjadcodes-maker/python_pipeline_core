from pathlib import Path
from logger import log_info, log_warning, log_error

def path_test(file_path):
    dir_path = Path(file_path).resolve()
    if not dir_path.exists():
        log_warning(f"The selected folder '{dir_path}' does not exist.")
        return f"The selected folder '{dir_path}' does not exist."
    
    elif not dir_path.is_dir():
        log_warning(f"'{dir_path}' you selected is not a folder.")
        return f"'{dir_path}' you selected is not a folder."
    else:
        file_list = list(dir_path.rglob("*"))
        detected_files = []

        try:
            for file in file_list:
                if file.is_file():
                    log_info(f"file detected: {file.name}")
                    detected_files.append(f"file detected: {file.name}")
            
            # If no files were found in the folder/subfolders
            if not detected_files:
                log_warning("No files found in the directory.")
                return "No files found in the directory."

            # Join all results into a single newline-separated string
            return detected_files

        except Exception as err:
            log_error(f"Failed scanning the {file.name}: {err}")
            return f"Failed scanning the directory: {err}"