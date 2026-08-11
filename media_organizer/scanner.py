from pathlib import Path
from logger import log_info, log_warning, log_error

def path_test(file_path: str):
    """
    Scans a folder path, logs discovered files, and returns a list of file log entries or an error message.
    """
    dir_path = Path(file_path).resolve()
    
    # Check if directory exists
    if not dir_path.exists():
        msg = f"The selected folder '{dir_path}' does not exist."
        log_warning(msg)
        return msg
    
    # Check if path is a directory
    if not dir_path.is_dir():
        msg = f"'{dir_path}' you selected is not a folder."
        log_warning(msg)
        return msg

    try:
        file_list = list(dir_path.rglob("*"))
        detected_files = []

        # Iterate over contents and log individual file occurrences
        for file in file_list:
            if file.is_file():
                msg = f"file detected: {file.name}"
                log_info(msg)
                detected_files.append(msg)
        
        # If no files were found
        if not detected_files:
            msg = "No files found in the directory."
            log_warning(msg)
            return msg

        return detected_files

    except Exception as err:
        err_msg = f"Failed scanning the directory: {err}"
        log_error(err_msg)
        return err_msg