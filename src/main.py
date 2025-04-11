import os
import yaml

def define_env(env):
    profile_dir = os.path.join(os.path.dirname(env.conf['config_file_path']),'docs','data','profiles')

    for file in os.listdir(profile_dir):
        filename = os.fsdecode(file)
        with open(os.path.join(profile_dir, filename), 'r') as f:
            team_data = yaml.safe_load(f)
        env.variables[os.path.splitext(filename)[0]] = team_data['team_members']
