from project.utils import load_config

project = 'eurostat_mapping'

config_data = load_config.load_config(project)

example_field = config_data['example_field']