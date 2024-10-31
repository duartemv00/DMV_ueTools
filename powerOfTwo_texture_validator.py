import unreal
import math

# Instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()

# Get the selected items
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
not_valid = 0

for asset in selected_assets:
    asset_name = asset.get_fname()
    asset_path = asset.get_path_name()
    
    try:
        x_size = asset.blueprint_get_size_x()
        y_size = asset.blueprint_get_size_y()
        
        # Check if both values are power of two
        is_x_valid = math.log(x_size, 2).is_integer()
        is_y_valid = math.log(y_size, 2).is_integer()
        
        if not is_x_valid or not is_y_valid:
            unreal.log_warning("Asset {} has invalid texture size ({}, {})".format(asset_name, x_size, y_size))
            unreal.log("It's path is {}".format(asset_path))
            not_valid += 1
    except Exception as err:
        unreal.log("{} is not a Texture - {}".format(asset_name, err))

unreal.log("{} checked, {} textures found problematic".format(num_assets, not_valid))