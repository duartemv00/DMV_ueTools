import unreal
import os

# Instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
cleaned = 0

# Hard coded parent path
parent_dir = "\\Game"

if num_assets > 0:
    # Get the path of the first selected asset
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(selected_assets[0])
    parent_dir = os.path.dirname(asset_path) # Strip the last part of the path

# Loop through the selected assets
for asset in selected_assets:
    # Get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)
    
    # Creating new path & Relocate assets
    try:
        new_path = os.path.join(parent_dir, class_name, asset_name)
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        cleaned += 1
    except Exception as err:
        unreal.log("Could not move asset {} to a new path".format(asset_name))
    
    unreal.log("Asset {} with class {}".format(asset_name, class_name))
    
unreal.log("Cleaned up {} of {} assets".format(cleaned, num_assets))