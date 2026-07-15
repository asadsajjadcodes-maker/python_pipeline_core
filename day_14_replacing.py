from pathlib import Path
log_path = Path("pipeline_log.txt")# create a path object for the log file
print("Reading and dynamically modifying the pipeline layout configuration.")
print("---------------------------------------------")
with open (log_path, mode="r", encoding="utf-8") as f:
    log_contant = f.read()
print("Content before modifying")
print(log_contant)
# Replace the string "SM_Castle_Gate" with "SM_Castle_Gate_V02" in the log content
updated_contant= log_contant.replace("SM_Castle_Gate", "SM_Castle_Gate_V02")
 
print("Modifying the log view..")
print(updated_contant)