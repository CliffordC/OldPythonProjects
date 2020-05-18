#! /usr/bin/env python

#This program takes files in a directory and renames them as a random number, this random number can be connected
#to the original file as the pairs are stored in a dictionary named key, can be used for blind analysis


import os
import random
import sys 
import json


#Change to match your directory
if os.path.exists('/Users/cliffordchi/Documents/Testground/'):


  Dir = os.listdir('/Users/cliffordchi/Documents/Testground/')

  Key = {}

  counter = 0

  for File in Dir :
    
    #takes a number in the range 1-100000 and chooses 42 samples randomly without replacement
    newname = str(random.randint(1,100))
    
    #takes name of original file and makes key with new file name in dictionary named Key
    Key[File] = newname
    
    os.rename('/Users/cliffordchi/Documents/Testground/' + File , newname)
    
    counter = counter + 1
    
  print (counter)

  #open the file in the mode that allows you to write to it (w) and (+) ensures you can read it too
  cheatsheet = open("cheatsheet.txt" , 'w+')

  #makes a new text file, names it cheat sheet, json helps open complex things ie the dictionary
  with open("cheatsheet.txt" , 'w') as file:
    file.write(json.dumps(Key))
else:
  print ("failed")