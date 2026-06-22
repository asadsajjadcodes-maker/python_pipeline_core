from pathlib import Path
asset_path =  Path("ground_mud_01_diffuse.png") 
print("Full name with extension: ")
#this will show the complete name of the asset with the extension
print(asset_path.name)
print("---------------------")
print("Pure asset name(The Stem):")
# this will show the name of the asset without the extension
print(asset_path.stem)
print("---------------------")
print("The extension type (The Suffix):")
# this will show the extension of the asset
print(asset_path.suffix)

