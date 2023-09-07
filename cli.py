import os 
from configparser import ConfigParser

import click

from .constants import (
    PARATOOLS_CONFIG_NAME,
    PARATOOLS_CONFIG_TEMPLATE
)

def get_directory_user_calling_from():
    return os.getcwd()

def get_user_home_directory():
    return os.path.expanduser('~')

def check_for_config_file():
    dir = get_directory_user_calling_from()
    config_file = os.path.join(dir, PARATOOLS_CONFIG_NAME)
    if os.path.exists(config_file):
        return True
    else:
        return False

def init():
    if check_for_config_file():
       print(f"Config file {PARATOOLS_CONFIG_NAME} already exists in current directory.") 
    else: 
        # Make default config file in current project
        config = ConfigParser()
        config.read_string(PARATOOLS_CONFIG_TEMPLATE)
        with open(PARATOOLS_CONFIG_NAME, 'w') as f:
            config.write(f)
            print(f"Config file {PARATOOLS_CONFIG_NAME} created in current directory.")
            print("Please edit the config file to point to your PARA directory.")
            print("Then run `paratools build` to build your library.")

def build():
    pass 

# click CLI with name paratools for above functions
@click.group()
def cli():
    pass

cli.add_command(init)
cli.add_command(build)

if __name__ == "__main__":
    cli()