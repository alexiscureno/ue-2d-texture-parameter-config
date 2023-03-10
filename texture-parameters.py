import unreal

# Get reference to the EditorAssetLibrary and StringLibrary classes
editor_asset_lib = unreal.EditorAssetLibrary()
string_lib = unreal.StringLibrary()

# Set the directory to search for textures and whether to include subfolders
source_dir = "/Game/"
include_subfolders = True

# Initialize a counter for the number of textures that are modified
set_textures = 0

# Get a list of assets in the directory and its subfolders
asset = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders)

# Define a list of patterns to match against the asset names
color_patterns = ["_ORM", "_OcclusionRoughnessMetallic", "_Metallic", "_Roughness", "_Mask", "_Albedo", "_BaseColor", "_Diffuse", "_Transparency"]

# Loop through the assets and check if they match any of the patterns
for asset in asset:
    for pattern in color_patterns:
        if string_lib.contains(asset, pattern):
            asset_obj = editor_asset_lib.load_asset(asset)
            asset_obj.set_editor_property("sRGB", False)
            asset_obj.set_editor_property("CompressionSettings", unreal.TextureCompressionSettings.TC_MASKS)

            # Log a message indicating which asset was modified
            unreal.log("Settings TC_Masks and turning off sRGB for asset {}".format(asset))
            set_textures += 1
            break
# Log the total number of textures that were modified
unreal.log("Linear color for matching textures set for {}".format(set_textures))
