#!/usr/bin/python
import os
import random
from pathlib import Path
import json

"""
This script creates a dictionary of old filenames matched with their new filenames.
Please edit the target_path before running this script.
"""


#target_path = '~/Documents/Testground'
target = '/Users/cliffordchi/Documents/Testground/'
target_path = Path('/Users/cliffordchi/Documents/Testground/')
destination = '/Users/cliffordchi/Documents/Newground/'
des = os.makedirs('/Users/cliffordchi/Documents/Newground')
dictionary = { }
cheat_sheet = open(target + "cheat_sheet.txt",'w+')

for file in os.listdir(target_path):
    random_num = str(random.randint(1,10000))
    dictionary[random_num] = file
    os.rename(target+file,target+random_num + ".txt")

with open(target + "cheat_sheet.txt",'w') as file:
    file.write(json.dumps(dictionary))



