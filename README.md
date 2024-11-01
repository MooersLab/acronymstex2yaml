![Version](https://img.shields.io/static/v1?label=acronymstex2yaml&message=0.1&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# Convert acronyms.tex to acronyms.yml

This script converts acronyms from the LaTeX glossaries package format to the YAML 
format for use in R Markdown and with the acronymsdown R package.

The output file is not true YAML format because dashed lines flank it.
It is a RMarkdown file.

The script reads an input file containing multiple acronyms in the LaTeX format, 
converts them, and writes the output to a specified yml file.
The conversion is not an exact match in terms of whitespacing compared to the 
examples given on the GitHub site for acronymsdown, but the output file is 
read correctly.

Usage:
    python acr2yaml.py <input_file> <output_file>


Example: 
   `python acr2yaml.py ~/glossaries/acronyms.tex acronyms.yml`

Example input and output files have been supplied above.

## Status

It works with Python 3.12.


## Update history

|Version      | Changes                                                                                                                                  | Date                 |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| Version 0.1 |   Added badges, funding, and update table.  Initial commit.                                                                              | 2024 November 1      |

## Sources of funding

- NIH: R01 CA242845
- NIH: R01 AI088011
- NIH: P30 CA225520 (PI: R. Mannel)
- NIH: P20 GM103640 and P30 GM145423 (PI: A. West)
