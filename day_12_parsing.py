from pathlib import Path
# Crating a path object to the log file 
log_path = Path("pipeline_log.txt")
print("Openig stream to parse the metadata......")
print("-----------------------------------")
# Opening the file and spliting the data 
with open (log_path, mode="r", encoding="utf-8") as f :
    for line in f :
        if ":" in line: # check if the line contains a colon, which indicates a label-value pair
            parts = line.split(":", maxsplit=1) # this will split only at the first colon, so we get the label and value correctly
            print(parts)
            label = parts[0].strip() # at index 0 will be the label
            value = parts[1].strip() # at index 1 will be the value
            print(f"Label found: {label}---> Value: {value}")
