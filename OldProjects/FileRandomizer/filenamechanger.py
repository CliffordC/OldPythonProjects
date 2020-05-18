#!/usr/bin/env python

#This program takes files in a directory and renames them as a random number, this random number can be connected
#to the original file as the pairs are stored in a dictionary named key, can be used for blind analysis


import os
import random
import json
import shutil



if os.path.exists('/Users/cliffordchi/Documents/Schmoo/'):


  Dir = os.listdir('/Users/cliffordchi/Documents/Schmoo/')

  Key = {}

  counter = 0

  for File in Dir:

    #takes a number in the range 1-100000 and chooses 42 samples randomly without replacement
    newname = str(random.randint(1,1000))

    #takes name of original file and makes key with new file name in dictionary named Key
    Key[File] = newname

    os.rename('/Users/cliffordchi/Documents/Schmoo/' + File , '/Users/cliffordchi/Documents/Schmoo_rand/'+newname + '.czi')
    #shutil.move('/Users/kristieshirley/pcfb/bookscripts/schmoo_backups/')
    counter = counter + 1
    
  print (counter)


  #open the file in the mode that allows you to write to it (w) and (+) ensures you can read it too
  cheatsheet = open("cheatsheet.txt" , 'w+')

  #makes a new text file, names it cheat sheet, json helps open complex things ie the dictionary
  with open('/Users/cliffordchi/Documents/Schmoo/'+'cheatsheet.txt' , 'w') as file:
    file.write(json.dumps(Key))
else:
  print ("failed")