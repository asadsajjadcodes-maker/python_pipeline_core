from pathlib import Path
log_path = Path("pipeline_log.txt")
print("Scaning log data for specific pipeline status flag....")
print("------------------------------------")
# opening the data to read
with open(log_path, mode="r", encoding="utf-8") as f:
    # Searching the data 
    for line in f:
        if "successfully" in line.lower(): # .lower make sure there will be no error 
            print(f"🟢 QA success:Validation found -> {line.strip()}")
        elif "error" in line.lower():
            print(f"🔴 QA faliure:Error found in line -> {line.strip()}")
        