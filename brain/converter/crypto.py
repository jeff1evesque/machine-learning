'''@crypto

This file contains various cryptography wrappers.


'''


import os
import hashlib
import base64

saltlength = 32

def hashpass(p):
    '''@hashpass

    This method returns a hash and salt from a password p
    
    @salt - a random string of saltlength bytes generated to hash the password
    
    '''
    salt = base64.b64encode(os.urandom(saltlength))
    return hashlib.sha512(salt + p).hexdigest()+"$"+salt

def verifypass(p, h):
    '''@verifypass

    This function verifies that a password p hashes to a hash h as 
    returned by hashpass.

    @h - hash extracted from the hash+salt
    @s - salt extracted from the hash+salt

    '''
    h,s = h.split('$')
    return hashlib.sha512(s + p).hexdigest() == h

#hash1 = hashpass('password')
#hash2 = hashpass('password')

#print 'hashpass returns different values for same password:', hash1 != hash2
#print 'hashpass verifies same password correctly for both hashes:', verifypass('password', hash1) and verifypass('password', hash2)

