import re
import yaml
import sys

"""
This script converts acronyms from the LaTeX glossaries package format to the YAML 
format for use in R Markdown and with the acronymsdown R package.
This is not true YAML format because it is flanked by dashed lines.
It reads an input file containing multiple acronyms in the LaTeX format, 
converts them, and writes the output to a specified yml file.
The conversion is not an exact match in terms of whitespacing to the 
examples given on the Github site for acronymsdown, but the output file is 
read correctly.

Usage:
    python convert_acronyms.py <input_file> <output_file>

Arguments:
    input_file  - The path to the input .tex file containing LaTeX acronyms.
    output_file - The path to the output .yml file where the converted acronyms will be saved.

Use of arcronyms.yml in R Markdown:
    - Add to YAML header of the Rmd file
    ```yaml
     acronyms:
      fromfile: ./acronyms.yml
    ```
    - Or for a list of acronym files
    ```yaml
    acronyms:
      fromfile:
        - ./acronyms1.yml
        - ./acronyms2.yml
    ```
    - Add acronyms in the text by adding `\acr{<KEY>}`. 

See https://github.com/rchaput/acronymsdown for more information.

Blaine Mooers, PhD
Department of Biochemistry and Physiology
College of Medicine
University of Oklahoma Health Sciences Center
Oklahoma City, OK

2024 November 1
"""

def convert_acronyms_to_yaml(input_file, output_file):
    acronyms_list = []

    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Extract acronyms from the lines
    for line in lines:
        match = re.match(r'\\newacronym\{(.+?)\}\{(.+?)\}\{(.+?)\}', line)
        if match:
            key, shortname, longname = match.groups()
            acronyms_list.append({
                'key': key,
                'shortname': shortname,
                'longname': longname
            })
    
    # Create the YAML structure
    acronyms_yaml = {
        'acronyms': {
          'keys': acronyms_list
        }
    }
    
    # Write the YAML structure to the output file with custom indentation
    with open(output_file, 'w') as file:
        file.write("---\n")
        yaml.dump(acronyms_yaml, file, sort_keys=False, default_flow_style=False, indent=4)
        file.write("---\n")
    
    # Adjust the indentation and strip extra spaces
    with open(output_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for line in lines:
            if line.strip().startswith('keys:'):
                file.write('  ' + line.lstrip())
            elif re.match(r'^\s{4}-\s{2}key:', line):
                file.write(line.replace('    -  key:', '- key:'))
            elif re.match(r'^\s{4}shortname:', line):
                file.write(line.replace('    shortname:', 'shortname:'))
            elif re.match(r'^\s{4}longname:', line):
                file.write(line.replace('    longname:', 'longname:'))
            else:
                file.write(line)
    
    print(f"Acronyms have been successfully converted and saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_acronyms.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_acronyms_to_yaml(input_file, output_file)
