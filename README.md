# Unreal Engine Texture Linear Color Setting Tool

## ue-2d-texture-parameter-config

This tool is a script written in Python using the Unreal Engine Python API to change the settings of textures in your Unreal Engine project.

# Requirements
* Unreal Engine 4.26 or later installed
* Python 3.7 or later installed
* unreal Python module installed

# Installation
1. Clone this repository or download the ZIP archive and extract its contents.
2. Open your Unreal Engine project.
3. In the main menu, select **File > Open Command Prompt** and run the following command:
```
python "path/to/TextureLinearColorSettingTool.py"
```
Replace ```path/to/TextureLinearColorSettingTool.py``` with the actual path to the script file.

# Usage
1. Modify the ```source_dir``` and ```include_subfolders``` variables in the script file to specify the directory and whether to include subfolders for the textures you want to modify.
2. Modify the ```color_patterns``` variable in the script file to specify the names of the textures that you want to modify.
3. Run the script file using the installation instructions above.

# Description
The script file searches for textures that match the patterns specified in ```color_patterns```. If a match is found, the script changes the ```sRGB``` and ```CompressionSettings``` properties of the texture to ```False``` and ```TC_MASKS```, respectively. These settings are more suitable for textures that represent data other than color, such as roughness or metalness values.

The script logs each texture that is modified and the total number of textures modified.
