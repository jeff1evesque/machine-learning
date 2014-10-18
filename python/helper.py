#!/usr/bin/python

## @helper.py
#  This file contains helper functions.
import hashlib, collections

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

## duplicate_list_index: returns a 'dictionary' of duplicate elements
#                        from the given list, 'list_to_check'.
#
#  for example:
#    list_to_check = list('ABRACADABR')
#
#  then, this method would return:
#    {'A': [0, 3, 5, 7], 'R': [2, 9], 'B': [1, 8], 'C': [4], 'D': [6]}
def duplicate_list_index(list_to_check):
  # store each element instance into dictionary
  dict_duplicates = collections.defaultdict(list_to_check)
  for index, value in enumerate(list_to_check):
    dic_duplicates[value].append(index)

  # remove non-duplicates from dictionary
  for key, value in dic_duplicates.iteritems():
    if ( len(value) <= 1 ):
      del dic_duplicates[key]
  return duplicates
