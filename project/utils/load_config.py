import os
import logging
import yaml

CONFIG_DIR = os.environ['CONFIG_PATH']

def load_config(project_name):
    config_path = os.path.join(CONFIG_DIR, f'{project_name}_config.yml')
    try:
        with open(config_path) as file:
            config_data = yaml.safe_load(file)
            return config_data
    except FileNotFoundError:
        logging.error(f"No such file or directory: {config_path}")
        raise FileNotFoundError(f"No such file or directory: {config_path}")


