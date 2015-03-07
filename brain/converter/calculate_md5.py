#!/usr/bin/python

## @calculate_md5.py
#  This file converts a given object to a hash value equivalent.
import hashlib
from collections import defaultdict

## calculate_md5: Convert the contents of a given object, to a hash value
#                 equivalent.
#
#  @md5.update, generate an md5 checksum fingerprint, of the given file. Calling
#      this method repeatedly, is equivalent to a single call with the concatenation
#      of all arguments:
#
#          md5.update(a), md5.update(b)
#
#      is equivalent to the following:
#
#          md5.update(a+b)
#
#      In some cases, the entire file is too large as a single argument to the
#      checksum update operation. Therefore, it is best practice to break the
#      operation into smaller chunks.
#
#  @block_size, the block size to break the supplied object (item).
#
#  @hr, determines whether to use the default 'digest' method, or to use the
#      'hexdigest' algorithm.
#
#  Note: block size directly depends on the block size of the filesystem.
def calculate_md5(item, block_size=256*128, hr=False):
  md5 = hashlib.md5()
  # use lambda anonymous function to iterate given object
  for chunk in iter(lambda: item.read(block_size), b''):
    md5.update(chunk)
  # return the digest of strings passed into 'update'
  if hr:
    return md5.hexdigest()
  return md5.digest()
