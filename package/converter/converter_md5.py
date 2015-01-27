#!/usr/bin/python

## @converter_md5.py
#  This file contains helper functions.
import hashlib, collections
from collections import defaultdict

## md5_for_file: Convert the contents of a given file to a hash value,
#                equivalent. Note, block size directly depends on the
#                block size of the filesystem.
def md5_for_file(path, block_size=256*128, hr=False):
  md5 = hashlib.md5()
  with open(path,'rb') as f: 
    for chunk in iter(lambda: f.read(block_size), b''): 
      md5.update(chunk)
  if hr:
    return md5.hexdigest()
  return md5.digest()

## duplicate_list_index: given a list, return a dictionary, with the 'key' being the list
#                        elements (unique, not duplicated), and the corresponding dictionary
#                        'value' being a list containing the index location of each instance.
#
#  for example:
#    list_to_check = list('ABRACADABR')
#
#  then, this method would return the following dictionary:
#    {'A': [0, 3, 5, 7], 'R': [2, 9], 'B': [1, 8], 'C': [4], 'D': [6]}
def duplicate_list_index(list_to_check):
  # store each element instance into dictionary
  dict_duplicates = collections.defaultdict(list)
  for key, value in enumerate(list_to_check):
    dict_duplicates[value].append(key)

  # remove non-duplicates from dictionary
  for key, value in dict_duplicates.items():
    if ( len(value) <= 1 ):
      del dict_duplicates[key]
  return dict_duplicates
