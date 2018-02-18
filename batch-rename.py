# Cameron M Merrick
# 2.13.2018
# filenameParser.py
# Script to rename a batch selection of files in a directory

import os
import sys

targetDir = sys.argv[1]
os.chdir(str(targetDir))

for f in os.listdir():
    # Split off the extension from the filename
    file_name, file_ext = os.path.splitext(f)
    # Select the numerical value at the end of the title
    num_in_title = str(file_name[-5:])
    file_name = num_in_title + '-' + file_name[:-6] + file_ext
    # os.rename(f, file_name)
    print('Renaming ' + f + ' to ' + file_name + '...Done!')
