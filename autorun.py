import os
import yaml
import subprocess
from wsgi import app
from yaml.loader import SafeLoader


def run_server(path, env):

    """Runs the flask server. If the enviroment is in development mode - """
    """All tests are executed before running server"""

    with open(path, 'r') as file:
        broke = False
        command_list = yaml.load(file, Loader=SafeLoader)[env]
        for command in command_list:
            if broke:
                break
            for run in command['run']:
                if run in app.config['ALLOWED_COMMANDS']:
                    process = subprocess.run(run, shell=True)
                    print('\n')
                    if process.returncode == 1:
                        broke = True
                        break
                else:
                    raise Exception('Invalid command')
    return broke


y_path = app.config['YAML_FILE']
environment = os.environ.get('FLASK_ENV')
run_server(y_path, environment)
