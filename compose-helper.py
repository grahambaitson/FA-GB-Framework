#!/usr/bin/env python
import os
import sys
import yaml

from compose.cli.command import project_from_options
from compose.config.config import load, ConfigDetails, ConfigFile


def get_project(config_details):
    return project_from_options(config_details.working_dir,
                                {'--file': [f.filename for f in config_details.config_files]})

def get_image_names(project):
    return [service.image_name for service in project.services]

def get_production_config(project, compose_file):
    names = {service.name: service.image_name for service in project.services}

    with open(compose_file) as f:
        config = yaml.safe_load(f)

    for name in config['services']:
        service = config['services'][name]
        if 'build' in service:
            service.pop('build')
            service['image'] = names[name]
    return yaml.safe_dump(config, default_flow_style=False, indent=2, width=80)


if __name__ == "__main__":
    n = len(sys.argv)
    if n < 2:
        raise ValueError("Expected at least two arguments, but got %d" % n)

    command = sys.argv[1]
    files = sys.argv[2:]

    project_dir = os.getcwd()
    config_details = ConfigDetails(project_dir, map(ConfigFile.from_filename, files))
    project = get_project(config_details)

    if command == "images":
        print "\n".join(get_image_names(project))
    elif command == "file":
        if len(files) > 1:
            raise ValueError("Expected just one file, but got %d" % len(files))
        print get_production_config(project, files[0])
    else:
        raise ValueError("Bad command: %s" % command)
