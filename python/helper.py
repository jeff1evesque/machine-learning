#!/usr/bin/python

## @helper.py
#  This file contains helper functions.
import hashlib, collections

## md5_for_file: Convert a file to a hash value, equivalent. Note,
#                block size directly depends on the block size of
#                the filesystem.
def md5_for_file(path, block_size=256*128, hr=False):
  md5 = hashlib.md5()
  with open(path,'rb') as f: 
    for chunk in iter(lambda: f.read(block_size), b''): 
      md5.update(chunk)
  if hr:
    return md5.hexdigest()
  return md5.digest()

def duplicate_list_index(list_to_check):
