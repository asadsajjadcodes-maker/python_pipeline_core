from pathlib import Path
current_repo = Path("")
print("Printing only the python files using .glob(): ")
print("--------------------------------")
for py_files in current_repo.glob("*.py"):
    print(f"Python asset found:{py_files.name}")