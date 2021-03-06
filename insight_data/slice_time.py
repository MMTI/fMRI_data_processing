"""
    Developed by Sameera K. Abeykoon (December 5th 2018)
    To extract slice timing infomation from .json files
    and save it a txt file

"""

import os, io
import numpy as np
import json
import sys
from six.moves import input

if len(sys.argv)<2:
    data_path = input("Enter the json files path ? ")
else:
    data_path = sys.argv[1]


json_files = [f for f in os.listdir(data_path) if (f.endswith('.json') and 'fMRI' in f)]

for j_file in json_files:
    # get a new file to save the slice timing information
    file_name = os.path.splitext(os.path.basename(j_file))[0]
    new_file = data_path + "/" + file_name + ".txt"
    print (j_file)
    # open the .json file
    j_filepath = data_path + "/" + j_file
    input_file = open(j_filepath, 'r')
    json_decode = json.load(input_file)

    # get the Slice Timings to a list
    y = json_decode['SliceTiming']
    # remove brackets and commas
    X = ' '.join( str(a) for a in y )
    
    # save the slice timing infomation to new file
    with open(new_file, 'w') as f: 
        f.write(X) 
