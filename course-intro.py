#!/usr/bin/env python

import sys
import yaml
from jinja2 import Environment, FileSystemLoader

usage_msg = f"Usage: {sys.argv[0]} FILE...\nwith FILE the name of a YAML file containing info about the course"
course_info_template = "course-intro.html.j2"

def generate_intro_html(file_name):
    ## Read data from YAML file
    course_info = {}
    with open(file_name) as info_file:
        course_info = yaml.full_load(info_file)

    ## Read HTML template
    template = Environment(loader=FileSystemLoader(".")).get_template(course_info_template)

    ## Emit HTML code
    output_file_name = file_name.replace("yml", "html")
    print(f"Processing {file_name} -> {output_file_name}")
    with open(output_file_name, "w") as html_file:
        html_file.write(template.render(course_info))

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        raise SystemExit(f"Not enough arguments, at least 1 expected\n{usage_msg}")
    files = sys.argv[1:]
    
    for file in files:
        generate_intro_html(file)
