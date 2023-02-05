from pelicanconf import * #get all my config variables
my_config = globals()
import pelican
import glob

default_config = pelican.settings.DEFAULT_CONFIG
#fill in the custom config variables

for key in default_config.keys():
    if key in my_config.keys():
        print('Overriding key', key)
        default_config[key] = my_config[key]
my_config = default_config


theme_dir_list = glob.glob('pelican-themes/*')
# for theme in theme_dir_list:
#     print(theme)
# theme_names = [theme.split('\\')[1] for theme in theme_dir_list]

# class my_arg:
#     def __init__(self, settings) -> None:
#         self.settings = settings
#         self.path = None
#         self.output = None
#         self.theme = None
#         self.delete_outputdir = None
#         self.ignore_cache = None
#         self.cache_path = None
#         self.selected_paths = None
#         self.relative_paths = None
#         self.port = None
#         self.bind = None
#         self.verbosity = pelican.logging.INFO
# args = my_arg('pelicanconf.py')
pelican_obj, settings = pelican.get_instance(pelican.parse_arguments()) #get the default settings

for key in settings.keys():
    if key in my_config.keys():
        print('Overriding key', key)
        settings[key] = my_config[key]

pelican_obj = pelican.Pelican(my_config)
pelican_obj.run()