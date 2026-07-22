import json
from pathlib import Path

def safe_save_json(data, file_path, indent=4):

    target_path = Path(file_path)
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open (target_path, mode="w",encoding="utf-8") as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as error:
        print(f"❌Error:  [{file_path}]: {error}")
        return False

print("--------------------")

sample_data = {
    "asset_name": "SM_Castle_Gate_V",
    "status": "ready_for_engine",
    "export_count": 1
}
print("proccessing..........")
for i in range(101):
    output_file =f"test_batch_json_files/config_{i}.json"
    sample_data["asset_name"] =f"SM_Castle_Gate_V{i}"
    safe_save_json(sample_data, output_file)
print("done")
    