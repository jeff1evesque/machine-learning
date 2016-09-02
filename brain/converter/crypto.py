'''@crypto

This file contains various cryptography wrappers.


'''


import os
import hashlib
import base64

saltlength = 32

# returns a hash and salt from a password p
def hashpass(p):
    salt = base64.b64encode(os.urandom(saltlength))
    return hashlib.sha512(salt + p).hexdigest()+"$"+salt

# verifies that a password p hashes to a hash h
def verifypass(p, h):
    h,s = h.split('$')
    return hashlib.sha512(s + p).hexdigest() == h

#hash1 = hashpass('password')
#hash2 = hashpass('password')

#print 'hashpass returns different values for same password:', hash1 != hash2
#print 'hashpass verifies same password correctly for both hashes:', verifypass('password', hash1) and verifypass('password', hash2)

