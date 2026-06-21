# bringing the pathlib module 
from pathlib import Path
# raw text 
raw_1 = "rock_texture.png"
# converting raw text into a smart object using Path 
smart_file = Path(raw_1) 
print("This is just a raw text:")
print(raw_1)
print("-------------------------------------------")
print("This is a smart object")
print(smart_file.name)
print(smart_file.suffix)
print(smart_file.cwd())# This will show the current working directory 