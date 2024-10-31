import unreal

def rename_assets(search_pattern, replace_pattern, use_case):
    # instance of unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()
    
    # get selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0
    
    unreal.log("Selected assets: " + str(num_assets))
    
    # iterate over selected assets
    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)
        
        unreal.log("Asset name: " + asset_name)
        
        # check if asset name contains the to be replaced name
        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replace_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case=search_case)
            editor_util.rename_asset(asset, replace_name)
            
            replaced += 1
            unreal.log("{} was renamed to {}".format(asset_name, replace_name))
            
        else:
            unreal.log("{} did not match the search pattern, was skipped".format(asset_name))
        
        unreal.log("Total assets renamed: " + str(replaced))
   
rename_assets("Physics", "PhysicsSmall", False)