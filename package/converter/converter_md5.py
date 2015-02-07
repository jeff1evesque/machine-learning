#!/usr/bin/python

## @converter_md5.py
#  This file converts a given file to a hash value equivalent.
import hashlib
from collections import defaultdict

## md5_for_file: Convert the contents of a given file, from a supplied path,
#                to a hash value equivalent.
#
#  Note: block size directly depends on the block size of the filesystem.
def md5_for_file(path, block_size=256*128, hr=False):
  md5 = hashlib.md5()
  with open(path,'rb') as f: 
    for chunk in iter(lambda: f.read(block_size), b''): 
      md5.update(chunk)
  if hr:
    return md5.hexdigest()
  return md5.digest()
