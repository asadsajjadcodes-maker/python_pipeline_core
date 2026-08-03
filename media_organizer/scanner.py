from pathlib import Path

def path_test(file_path):
    dir_path = Path(file_path).resolve()
    if not dir_path.exists():
        return f"The selected folder '{dir_path}' does not exist."
    elif not dir_path.is_dir():
        return f"'{dir_path}' you selected is not a folder."
    else:
        file_list = list(dir_path.rglob("*"))
        detected_files = []

        try:
            for file in file_list:
                if file.is_file():
                    detected_files.append(f"file detected: {file.name}")
            
            # If no files were found in the folder/subfolders
            if not detected_files:
                return "No files found in the directory."

            # Join all results into a single newline-separated string
            return detected_files

        except Exception as err:
            return f"Failed scanning the directory: {err}"