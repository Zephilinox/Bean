
# Point export_dir to the folder you will be keeping your module, ensure it exists first.
# Make sure you use forward slashes (/) and NOT backward slashes (\)

export_dir = "Output/"
#export_dir = "C:/Program Files/Mount&Blade/Modules/Native/"

# If you don't want some of the neat features of [swysdk]
# you can disable them here: True/False, case sensitive.
swysdk = {
    'enable_obfuscation': True,
    'enable_optimizations': True,
    'enable_caching': True,
    'enable_wse': False,
}